from typing import Protocol
from .schemas import PetOwnerCreate
from .models import PetOwner


class ExternalPetOwnerService(Protocol):
    def create_pet_owner(self, *, petowner_new: PetOwnerCreate) -> PetOwner: ...


class InternalPetOwnerService(ExternalPetOwnerService, Protocol):
    pass
