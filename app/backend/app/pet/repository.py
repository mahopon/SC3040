from sqlalchemy.orm import Session
from .models import Pet


def create_pet(*, db_session: Session, pet_new: Pet) -> None:
    db_session.add(pet_new)
