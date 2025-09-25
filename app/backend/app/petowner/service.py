from .protocols import InternalPetOwnerService
from .repository import PetOwnerRepository
from .schemas import PetOwnerCreate
from .models import PetOwner
from uuid import UUID


class PetOwnerService(InternalPetOwnerService):
    def __init__(self, repo: PetOwnerRepository):
        self.repo = repo

    def create_pet_owner(self, *, petowner_new: PetOwnerCreate) -> PetOwner:
        petowner = PetOwner(**petowner_new.model_dump())
        self.repo.create_petowner(petowner_new=petowner)
        return petowner

    def delete_pet_owner(self, *, petowner_id: UUID) -> None:
        self.repo.delete_petowner(petowner_id=petowner_id)
