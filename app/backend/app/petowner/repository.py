from sqlalchemy.orm import Session
from sqlalchemy import delete
from .models import PetOwner
from app.util.repository import db_add
from uuid import UUID


class PetOwnerRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_petowner(self, *, petowner_new: PetOwner) -> None:
        db_add(self.db_session, petowner_new)

    def delete_petowner(self, *, petowner_id: UUID) -> None:
        stmt = delete(PetOwner).where(PetOwner.id == petowner_id)
        self.db_session.execute(stmt)
