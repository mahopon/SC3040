from sqlalchemy.orm import Session
from .models import PetCareTaker


def create_petcaretaker(*, db_session: Session, petcaretaker_new: PetCareTaker) -> None:
    db_session.add(petcaretaker_new)
