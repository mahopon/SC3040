from sqlalchemy.orm import Session
from .models import Auth, AuthSession
from .schemas import AuthRegister, AuthPasswordUpdate, OAuthOutcome, OAuthRegister
from .repository import get_auth_by_email, create_auth, create_session, get_auth_by_id, get_auth_by_session_id
from uuid import UUID
from authlib.integrations.starlette_client import OAuth
from fastapi.requests import Request
from .exceptions import InvalidCredentials, EmailAlreadyExists, PasswordMismatch


def login(*, db_session: Session, email: str, password: str) -> Auth:
    """Returns an auth object based on email"""
    auth = get_auth_by_email(db_session=db_session, email=email)
    if auth and auth.verify_password(password):
        return auth
    raise InvalidCredentials("Invalid credentials")


def retrieve_auth_by_session(*, db_session: Session, session_id: str) -> Auth:
    auth = get_auth_by_session_id(db_session=db_session, session_id=session_id)
    if not auth:
        raise InvalidCredentials("Session doen't exist")
    return auth


def register_web(*, db_session: Session, auth_in: AuthRegister) -> Auth:
    """Create an auth object using details from frontend"""
    auth = get_auth_by_email(db_session=db_session, email=auth_in.email)
    if auth:
        raise EmailAlreadyExists("Email is already in use")
    new_auth = Auth(**auth_in.model_dump(exclude={"password", "name", "dob"}))
    if auth_in.password:
        new_auth.set_password(auth_in.password.get_secret_value())
    create_auth(db_session=db_session, auth_new=new_auth)
    return new_auth


def register_oauth(*, db_session: Session, auth_in: OAuthRegister) -> Auth:
    """Create an auth object using details from OAuth authentication"""
    new_auth = Auth(**auth_in.model_dump(exclude={"name"}))
    create_auth(db_session=db_session, auth_new=new_auth)
    return new_auth


def create_session_id(*, db_session: Session, auth: Auth) -> AuthSession:
    """Create session"""
    session_id = auth.token
    session: AuthSession = AuthSession(auth=auth, session_id=session_id)
    create_session(db_session=db_session, session_new=session)
    return session


def change_password(*, db_session: Session, user_id: UUID, auth_pw_in: AuthPasswordUpdate) -> None:
    """Change password of user. If password is None (OAuth registration), then set to new password. Else verify current password matches old password and change to new password"""
    auth: Auth | None = get_auth_by_id(db_session=db_session, id=user_id)
    if auth:
        if auth.password is None:
            auth.set_password(auth_pw_in.new_password.get_secret_value())
            return
        else:
            isOldPWMatch = auth.verify_password(auth_pw_in.old_password.get_secret_value())
            if isOldPWMatch:
                auth.set_password(auth_pw_in.new_password.get_secret_value())
                return
            else:
                raise PasswordMismatch("Old password is wrong")
    raise InvalidCredentials("User does not exist")


async def process_oauth_callback(db_session: Session, oauth: OAuth, request: Request) -> OAuthOutcome:
    """Process OAuth2 JWT token"""
    token = await oauth.google.authorize_access_token(request)
    email = token["userinfo"]["email"]
    name = token["userinfo"]["name"]

    auth = get_auth_by_email(db_session=db_session, email=email)
    if auth:
        return OAuthOutcome(existing_auth=auth)

    return OAuthOutcome(registration=OAuthRegister(email=email, name=name))
