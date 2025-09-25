from typing import Protocol
from .schemas import PetCreate
from uuid import UUID


class ExternalPetService(Protocol):
    """
    Protocol defining the external interface for pet services.

    Intended for use by modules or routes that interact with pet functionality.
    """

    def create_pet(self, *, owner_id: UUID, pet_new: PetCreate) -> None:
        """
        Create a new pet for the given owner.

        Args:
            owner_id (UUID): The ID of the pet owner.
            pet_new (PetCreate): Schema containing the pet's data.
        """


class InternalPetService(ExternalPetService, Protocol):
    """
    Protocol for internal pet service operations.

    Currently mirrors ExternalPetService, but can be extended with internal-only methods in the future.
    """

    pass
