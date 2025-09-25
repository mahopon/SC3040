from typing import Protocol, List
from uuid import UUID
from .schemas import OfferedServiceCreate, OfferedService as OfferedServiceDTO, Service as ServiceDTO


class ExternalServiceService(Protocol):
    """
    External-facing service interface for managing offered services.
    """

    def create_offered_service(self, *, profile_id: UUID, offered_service_req: OfferedServiceCreate) -> None: ...


class InternalServiceService(ExternalServiceService, Protocol):
    """
    Internal-facing service interface with extended operations.
    """

    def get_offered_services(self, *, profile_id: UUID) -> List[OfferedServiceDTO]: ...
    def get_services(self) -> List[ServiceDTO]: ...
