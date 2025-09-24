from sqlalchemy.orm import Session
from sqlalchemy import update
from .models import Profile
from .schemas import ProfileInitialUpdate, ProfileUpdate
from uuid import UUID
from app.util.repository import db_add, get_by_field


class ProfileRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_by_id(self, profile_id: UUID) -> Profile | None:
        return get_by_field(self.db_session, Profile, "id", profile_id)

    def create_profile(self, profile_new: Profile) -> None:
        db_add(self.db_session, profile_new)

    def onboard_profile(self, profile_id: UUID, profile_update: ProfileInitialUpdate) -> None:
        values = profile_update.model_dump()
        stmt = update(Profile).where(Profile.id == profile_id).values(**values, setup=(Profile.setup | True))  # noqa
        self.db_session.execute(stmt)

    def update_profile(self, profile_id: UUID, profile_update: ProfileUpdate) -> None:
        values = profile_update.model_dump(exclude_unset=True)
        stmt = update(Profile).where(Profile.id == profile_id).values(**values)
        self.db_session.execute(stmt)
