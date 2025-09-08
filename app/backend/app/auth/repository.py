from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Auth, AuthSession
from uuid import UUID


def get_auth_by_email(*, db_session: Session, email: str) -> Auth | None:
    stmt = select(Auth).where(Auth.email == email)
    return db_session.execute(stmt).scalar_one_or_none()


def get_auth_by_id(*, db_session: Session, id: UUID) -> Auth | None:
    stmt = select(Auth).where(Auth.id == id)
    return db_session.execute(stmt).scalar_one_or_none()


def create_auth(*, db_session: Session, auth_new: Auth) -> None:
    db_session.add(auth_new)


def create_session(*, db_session: Session, session_new: AuthSession) -> None:
    db_session.add(session_new)
