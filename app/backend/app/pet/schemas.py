from pydantic import BaseModel
from typing import Optional


class PetCreate(BaseModel):
    name: str
    species: str
    breed: str
    age: int
    health: Optional[str] = None
    preferences: Optional[str] = None
