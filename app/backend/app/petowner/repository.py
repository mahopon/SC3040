from sqlalchemy.orm import Session
from .models import PetOwner


def create_petowner(*, db_session: Session, petowner_new: PetOwner) -> None:
    db_session.add(petowner_new)
