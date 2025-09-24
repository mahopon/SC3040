from typing import Protocol
from .schemas import PetCreate
from uuid import UUID


class ExternalPetService(Protocol):
    def create_pet(self, *, owner_id: UUID, pet_new: PetCreate) -> None: ...


class InternalPetService(ExternalPetService, Protocol):
    pass
