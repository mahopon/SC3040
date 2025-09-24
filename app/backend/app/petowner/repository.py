from sqlalchemy.orm import Session
from .models import PetOwner
from app.util.repository import db_add


class PetOwnerRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_petowner(self, *, petowner_new: PetOwner) -> None:
        db_add(self.db_session, petowner_new)
