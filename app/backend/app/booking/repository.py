from sqlalchemy.orm import Session
from .models import ServiceBookingDay, ServiceBooking
from app.util.repository import db_add


class BookingRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_service_booking(self, *, service_booking_new: ServiceBooking) -> None:
        db_add(self.db_session, service_booking_new)

    def create_service_booking_day(self, *, booking_day_new: ServiceBookingDay) -> None:
        db_add(self.db_session, booking_day_new)
