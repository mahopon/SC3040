from sqlalchemy.orm import Session
from .models import Service, OfferedService, ServiceBooking, ServiceBookingDay


def create_service(*, db_session: Session, service_new: Service) -> None:
    db_session.add(service_new)


def create_offered_service(*, db_session: Session, offered_service_new: OfferedService) -> None:
    db_session.add(offered_service_new)


def create_service_booking(*, db_session: Session, service_booking_new: ServiceBooking) -> None:
    db_session.add(service_booking_new)


def create_service_booking_day(*, db_session: Session, booking_day_new: ServiceBookingDay) -> None:
    db_session.add(booking_day_new)
