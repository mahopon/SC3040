from .protocols import InternalPetOwnerService
from .repository import PetOwnerRepository
from .schemas import PetOwnerCreate
from .models import PetOwner


class PetOwnerService(InternalPetOwnerService):
    def __init__(self, repo: PetOwnerRepository):
        self.repo = repo

    def create_pet_owner(self, *, petowner_new: PetOwnerCreate) -> PetOwner:
        petowner = PetOwner(**petowner_new.model_dump())
        self.repo.create_petowner(petowner_new=petowner)
        return petowner
