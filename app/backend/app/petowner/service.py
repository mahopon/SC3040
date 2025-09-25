from .protocols import InternalPetOwnerService
from .repository import PetOwnerRepository
from .schemas import PetOwnerCreate
from .models import PetOwner
from uuid import UUID


class PetOwnerService(InternalPetOwnerService):
    """
    Concrete implementation of the InternalPetOwnerService protocol.

    Handles creation and deletion of PetOwner entities using the repository pattern.
    """

    def __init__(self, repo: PetOwnerRepository):
        """
        Initialize PetOwnerService with a repository.

        Args:
            repo (PetOwnerRepository): Repository for database operations on PetOwner.
        """
        self.repo = repo

    def create_pet_owner(self, *, petowner_new: PetOwnerCreate) -> PetOwner:
        """
        Create a new PetOwner and persist it to the database.

        Args:
            petowner_new (PetOwnerCreate): Data for the new PetOwner.

        Returns:
            PetOwner: The created PetOwner instance.
        """
        petowner = PetOwner(**petowner_new.model_dump())
        self.repo.create_petowner(petowner_new=petowner)
        return petowner

    def delete_pet_owner(self, *, petowner_id: UUID) -> None:
        """
        Delete an existing PetOwner by their ID.

        Args:
            petowner_id (UUID): The ID of the PetOwner to delete.
        """
        self.repo.delete_petowner(petowner_id=petowner_id)
