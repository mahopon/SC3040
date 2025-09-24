from typing import Protocol, List
from uuid import UUID
from .schemas import OfferedServiceCreate, OfferedService, Service


class ExternalServiceService(Protocol):
    def create_offered_service(self, *, profile_id: UUID, offered_service_req: OfferedServiceCreate) -> None: ...


class InternalServiceService(ExternalServiceService, Protocol):
    def get_offered_services(self, *, profile_id: UUID) -> List[OfferedService]: ...
    def get_services(self) -> List[Service]: ...
