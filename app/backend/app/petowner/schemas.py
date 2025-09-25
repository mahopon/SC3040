from pydantic import BaseModel
from uuid import UUID


class PetOwnerCreate(BaseModel):
    """
    Schema for creating a new PetOwner.

    Attributes:
        id (UUID): ID of the profile that this PetOwner is linked to.
    """

    id: UUID
