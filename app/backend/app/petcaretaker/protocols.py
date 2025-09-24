from typing import Protocol
from .schemas import PetCareTaker as PetCareTakerDTO, PetCareTakerCreate, PetCareTakerUpdate
from uuid import UUID


class ExternalPetCareTakerService(Protocol):
    def create_petcaretaker(self, *, petcaretaker_new: PetCareTakerCreate) -> None: ...
    def update_petcaretaker(self, *, petcaretaker_id: UUID, petcaretaker_update: PetCareTakerUpdate) -> None: ...


class InternalPetCareTakerService(ExternalPetCareTakerService, Protocol):
    def get_petcaretaker(self, *, petcaretaker_id: UUID) -> PetCareTakerDTO: ...
