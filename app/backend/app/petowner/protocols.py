from typing import Protocol
from .schemas import PetOwnerCreate
from .models import PetOwner
from uuid import UUID


class ExternalPetOwnerService(Protocol):
    def create_pet_owner(self, *, petowner_new: PetOwnerCreate) -> PetOwner: ...
    def delete_pet_owner(self, *, petowner_id: UUID) -> None: ...


class InternalPetOwnerService(ExternalPetOwnerService, Protocol):
    pass
