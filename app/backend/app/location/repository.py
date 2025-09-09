from sqlalchemy.orm import Session
from .models import Location


def create_location(*, db_session: Session, location_new: Location) -> None:
    db_session.add(location_new)
