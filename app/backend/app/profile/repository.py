from sqlalchemy.orm import Session
from sqlalchemy import select, update
from .models import Profile
from .schemas import ProfileSetup
from uuid import UUID


def get_profile_by_id(*, db_session: Session, profile_id: UUID) -> Profile | None:
    stmt = select(Profile).where(Profile.id == profile_id)
    profile = db_session.execute(stmt).scalar_one_or_none()
    return profile


def create_profile(*, db_session: Session, profile_new: Profile) -> None:
    db_session.add(profile_new)


def setup_profile(*, db_session: Session, profile: ProfileSetup) -> None:
    stmt = update(Profile).where(Profile.id == profile.id).values(**profile.model_dump())
    db_session.execute(stmt)
