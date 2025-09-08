from fastapi import APIRouter, status, Path, Body
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from .schemas import (
    AuthLoginResponse,
    AuthLogin,
    AuthRegister,
    AuthRegisterResponse,
    AuthPasswordUpdate,
)
from app.database.core import DbSession
from .service import login, create_session_id, register_web, register_oauth, change_password, process_oauth_callback
from .models import Auth, AuthSession
from uuid import UUID
from secrets import token_urlsafe
from .oauth2 import oauth
from typing import Any

auth_router = APIRouter()


@auth_router.post("/login", response_model=AuthLoginResponse)
def login_auth(auth_in: AuthLogin, db_session: DbSession) -> JSONResponse:
    auth: Auth = login(db_session=db_session, email=auth_in.email, password=auth_in.password)
    session: AuthSession = create_session_id(db_session=db_session, auth=auth)
    # TODO Get name from profile domain
    resp: AuthLoginResponse = AuthLoginResponse(user_id=auth.id, name="temp", token=session.session_id)
    return JSONResponse(content=resp.model_dump())


@auth_router.post("/register", response_model=AuthRegisterResponse)
def register_auth(auth_new: AuthRegister, db_session: DbSession) -> RedirectResponse:
    auth: Auth = register_web(db_session=db_session, auth_in=auth_new)  # noqa
    # TODO Add user profile creation
    return RedirectResponse(url="/auth/login", status_code=status.HTTP_303_SEE_OTHER)


@auth_router.patch(
    "/change-password/{user_id}", description="Send passwords as plaintext, censored values are not an issue"
)
def change_password_auth(
    db_session: DbSession,
    user_id: UUID = Path(...),
    pw_change: AuthPasswordUpdate = Body(...),
) -> Response:
    change_password(db_session=db_session, user_id=user_id, auth_pw_in=pw_change)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@auth_router.get("/login/google", description="Redirects to Google OAuth2 login")
async def login_google(request: Request) -> Any:
    state = token_urlsafe(32)
    request.session["oauth_state"] = state
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri, state=state)


@auth_router.get("/callback", name="auth_callback", description="Callback from OAuth2 authentication")
async def oauth_callback(request: Request, db_session: DbSession) -> RedirectResponse:
    state_in_session = request.session.get("oauth_state")
    query_state = request.query_params.get("state")

    if not state_in_session or state_in_session != query_state:
        raise HTTPException(status_code=400, detail="Invalid OAuth state")

    del request.session["oauth_state"]

    # Process and generate session_id
    auth_details = await process_oauth_callback(db_session=db_session, oauth=oauth, request=request)
    if auth_details.existing_auth:
        session = create_session_id(db_session=db_session, auth=auth_details.existing_auth)
    elif auth_details.registration:
        # TODO Create profile using registration details
        auth = register_oauth(db_session=db_session, auth_in=auth_details.registration)
        session = create_session_id(db_session=db_session, auth=auth)

    # Set session ID as HttpOnly cookie
    response = RedirectResponse(url="/home")
    response.set_cookie(
        key="session_id",
        value=session.session_id,
        httponly=True,
        secure=True,  # True in production with HTTPS
        max_age=31 * 60 * 60 * 24,  # 31 days
    )
    return response
