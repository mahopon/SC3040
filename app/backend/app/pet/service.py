from .protocols import InternalPetService
from .schemas import PetCreate
from .models import Pet
from .repository import PetRepository
from uuid import UUID


class PetService(InternalPetService):
    def __init__(self, repo: PetRepository):
        self.repo = repo

    def create_pet(self, *, owner_id: UUID, pet_new: PetCreate) -> None:
        new_pet = Pet(**pet_new.model_dump())
        new_pet.owner_id = owner_id
        self.repo.create_pet(pet_new=new_pet)
