from fastapi import status
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from app.database.core import DbSession
from .service import retrieve_auth_by_session
from uuid import UUID


async def get_id_from_session(request: Request, db_session: DbSession) -> UUID:
    session_id = request.state.session_id
    auth = retrieve_auth_by_session(db_session=db_session, session_id=session_id)
    if not auth:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return auth.id
