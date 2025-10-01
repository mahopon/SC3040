from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from .models import Service, OfferedService
from app.util.repository import db_add
from typing import List, Dict, Any
from uuid import UUID
from typing import Optional


class ServiceRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_service(self, *, service_new: Service) -> None:
        db_add(self.db_session, service_new)

    def create_offered_service(self, *, offered_service_new: OfferedService) -> None:
        db_add(self.db_session, offered_service_new)

    def get_offered_service_by_id(self, offered_service_id: int) -> Optional[OfferedService]:
        stmt = select(OfferedService).where(OfferedService.id == offered_service_id)
        return self.db_session.execute(stmt).scalar_one_or_none()

    def get_services(self) -> List[Service]:
        stmt = select(Service)
        return list(self.db_session.execute(stmt).scalars().all())

    def get_offered_service_by_service_caretaker_id(
        self, *, service_id: int, caretaker_id: UUID
    ) -> Optional[OfferedService]:
        stmt = select(OfferedService).where(
            OfferedService.service_id == service_id and OfferedService.caretaker_id == caretaker_id
        )
        return self.db_session.execute(stmt).scalar_one_or_none()

    def get_offered_services_by_profile_id(self, *, profile_id: UUID) -> List[OfferedService]:
        stmt = (
            select(OfferedService)
            .join(Service, OfferedService.service_id == Service.id)
            .where(OfferedService.caretaker_id == profile_id)
        )
        return list(self.db_session.execute(stmt).scalars().all())

    def get_offered_services(self) -> List[OfferedService]:
        stmt = select(OfferedService).join(Service, OfferedService.service_id == Service.id)
        return list(self.db_session.execute(stmt).scalars().all())

    def update_offered_service(self, offered_service_id: int, values: Dict[str, Any]) -> None:
        stmt = update(OfferedService).where(OfferedService.id == offered_service_id).values(**values)
        self.db_session.execute(stmt)

    def delete_offered_service(self, offered_service_id: int) -> None:
        stmt = delete(OfferedService).where(OfferedService.id == offered_service_id)
        self.db_session.execute(stmt)
