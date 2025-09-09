from sqlalchemy.orm import Session
from .models import Profile


def create_profile(*, db_session: Session, profile_new: Profile) -> None:
    db_session.add(profile_new)
