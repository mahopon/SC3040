from pydantic import BaseModel
from uuid import UUID


class PetOwnerCreate(BaseModel):
    id: UUID
