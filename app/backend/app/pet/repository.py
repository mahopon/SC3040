from sqlalchemy.orm import Session
from .models import Pet
from app.util.repository import db_add


class PetRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_pet(self, *, pet_new: Pet) -> None:
        db_add(self.db_session, pet_new)
