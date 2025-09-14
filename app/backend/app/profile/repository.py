from sqlalchemy.orm import Session
from sqlalchemy import update
from .models import Profile
from .schemas import ProfileSetup
from uuid import UUID
from app.util.repository import get_by_field, db_add


class ProfileRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_by_id(self, profile_id: UUID) -> Profile | None:
        return get_by_field(self.db_session, Profile, "id", profile_id)

    def create_profile(self, profile_new: Profile) -> None:
        db_add(self.db_session, profile_new)

    def update_initial(self, profile_setup: ProfileSetup) -> None:
        stmt = update(Profile).where(Profile.id == profile_setup.id).values(**profile_setup.model_dump())
        self.db_session.execute(stmt)
