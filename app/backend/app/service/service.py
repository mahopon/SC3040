from .repository import ServiceRepository
from uuid import UUID
from .schemas import OfferedServiceCreate, OfferedService as OfferedServiceDTO, Service as ServiceDTO
from .models import OfferedService
from typing import List


class ServiceService:
    def __init__(self, repo: ServiceRepository):
        self.repo = repo

    def create_offered_service(self, *, profile_id: UUID, offered_service_req: OfferedServiceCreate) -> None:
        new_offered_service = OfferedService(caretaker_id=profile_id, **offered_service_req.model_dump())
        self.repo.create_offered_service(offered_service_new=new_offered_service)

    def get_offered_services_by_profile_id(self, *, profile_id: UUID) -> List[OfferedServiceDTO]:
        all_services_by_profile = self.repo.get_offered_services_by_profile_id(profile_id=profile_id)
        dto_services = [OfferedServiceDTO.model_validate(svc) for svc in all_services_by_profile]
        return dto_services

    def get_services(self) -> List[ServiceDTO]:
        all_services = self.repo.get_services()
        dto_services = [ServiceDTO.model_validate(svc) for svc in all_services]
        return dto_services
