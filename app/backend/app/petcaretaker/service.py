from .protocols import InternalPetCareTakerService
from .repository import PetCareTakerRepository
from .models import PetCareTaker
from .schemas import PetCareTakerCreate, PetCareTaker as PetCareTakerDTO, PetCareTakerUpdate
from uuid import UUID
from .exceptions import PetCareTakerNotFound


class PetCareTakerService(InternalPetCareTakerService):
    def __init__(self, repo: PetCareTakerRepository):
        self.repo = repo

    def get_petcaretaker(self, *, petcaretaker_id: UUID) -> PetCareTakerDTO:
        petcaretaker = self.repo.get_petcaretaker_by_id(petcaretaker_id=petcaretaker_id)
        if not petcaretaker:
            raise PetCareTakerNotFound("PetCareTaker not found")
        return PetCareTakerDTO.model_validate(petcaretaker.dict())

    def create_petcaretaker(self, *, petcaretaker_new: PetCareTakerCreate) -> None:
        new_petcaretaker = PetCareTaker(**petcaretaker_new.model_dump())
        self.repo.create_petcaretaker(petcaretaker_new=new_petcaretaker)

    def update_petcaretaker(self, *, petcaretaker_id: UUID, petcaretaker_update: PetCareTakerUpdate) -> None:
        petcaretaker = self.repo.get_petcaretaker_by_id(petcaretaker_id=petcaretaker_id)
        if not petcaretaker:
            raise PetCareTakerNotFound("PetCareTaker not found")
        self.repo.update_petcaretaker(petcaretaker_id=petcaretaker_id, petcaretaker_update=petcaretaker_update)

    def delete_petcaretaker(self, *, petcaretaker_id: UUID) -> None:
        self.repo.delete_petcaretaker(petcaretaker_id=petcaretaker_id)
