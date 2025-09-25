from .protocols import InternalPetService
from .schemas import PetCreate
from .models import Pet
from .repository import PetRepository
from uuid import UUID


class PetService(InternalPetService):
    """
    Concrete implementation of the InternalPetService protocol.

    Handles creation of pets using the repository pattern.
    """

    def __init__(self, repo: PetRepository):
        """
        Initialize PetService with a repository.

        Args:
            repo (PetRepository): Repository for database operations on pets.
        """
        self.repo = repo

    def create_pet(self, *, owner_id: UUID, pet_new: PetCreate) -> None:
        """
        Create a new pet for the specified owner and persist it to the database.

        Args:
            owner_id (UUID): The ID of the pet owner.
            pet_new (PetCreate): Data for the new pet.
        """
        new_pet = Pet(**pet_new.model_dump())
        new_pet.owner_id = owner_id
        self.repo.create_pet(pet_new=new_pet)
