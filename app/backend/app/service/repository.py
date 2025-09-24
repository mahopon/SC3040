from sqlalchemy.orm import Session
from sqlalchemy import select
from .models import Service, OfferedService, ServiceBooking, ServiceBookingDay
from app.util.repository import db_add
from typing import List
from uuid import UUID


class ServiceRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_service(self, *, service_new: Service) -> None:
        db_add(self.db_session, service_new)

    def create_offered_service(self, *, offered_service_new: OfferedService) -> None:
        db_add(self.db_session, offered_service_new)

    def create_service_booking(self, *, service_booking_new: ServiceBooking) -> None:
        db_add(self.db_session, service_booking_new)

    def create_service_booking_day(self, *, booking_day_new: ServiceBookingDay) -> None:
        db_add(self.db_session, booking_day_new)

    def get_services(self) -> List[Service]:
        stmt = select(Service)
        return list(self.db_session.execute(stmt).scalars().all())

    def get_offered_services_by_profile_id(self, *, profile_id: UUID) -> List[OfferedService]:
        stmt = select(OfferedService).where(OfferedService.caretaker_id == profile_id)
        return list(self.db_session.execute(stmt).scalars().all())
