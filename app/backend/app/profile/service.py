from sqlalchemy.orm import Session
from .models import Profile
from .schemas import ProfileRegister, ProfileSetup
from .repository import create_profile, setup_profile, get_profile_by_id
from uuid import UUID
from .exceptions import ProfileNotExists


def get_profile(*, db_session: Session, profile_id: UUID) -> Profile:
    profile = get_profile_by_id(db_session=db_session, profile_id=profile_id)
    if not profile:
        raise ProfileNotExists("Profile does not exist")
    return profile


def register_profile(*, db_session: Session, profile_new: ProfileRegister) -> Profile:
    new_profile = Profile(**profile_new.model_dump())
    create_profile(db_session=db_session, profile_new=new_profile)
    return new_profile


def initial_setup_profile(*, db_session: Session, profile: ProfileSetup) -> None:
    setup_profile(db_session=db_session, profile=profile)
