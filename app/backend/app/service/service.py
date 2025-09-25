from .repository import ServiceRepository
from uuid import UUID
from .schemas import OfferedServiceCreate, OfferedService as OfferedServiceDTO, Service as ServiceDTO
from .models import OfferedService
from typing import List


class ServiceService:
    """
    Concrete implementation of Service-related operations.
    """

    def __init__(self, repo: ServiceRepository):
        """
        Args:
            repo: Repository handling database interactions for services.
        """
        self.repo = repo

    def create_offered_service(self, *, profile_id: UUID, offered_service_req: OfferedServiceCreate) -> None:
        """
        Create a new offered service for a caretaker.
        """
        new_offered_service = OfferedService(caretaker_id=profile_id, **offered_service_req.model_dump())
        self.repo.create_offered_service(offered_service_new=new_offered_service)

    def get_offered_services_by_profile_id(self, *, profile_id: UUID) -> List[OfferedServiceDTO]:
        """
        Retrieve all offered services for a specific caretaker.
        """
        all_services = self.repo.get_offered_services_by_profile_id(profile_id=profile_id)
        return [OfferedServiceDTO.model_validate(svc) for svc in all_services]

    def get_services(self) -> List[ServiceDTO]:
        """
        Retrieve all available services.
        """
        all_services = self.repo.get_services()
        return [ServiceDTO.model_validate(svc) for svc in all_services]
