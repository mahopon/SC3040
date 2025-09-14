from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Literal
from datetime import datetime
from .enums import Gender


class ProfileDTO(BaseModel):
    name: str
    dob: Optional[datetime] = None
    gender: Optional[Gender] = None

    model_config = {"from_attributes": True}


class ProfileRegister(ProfileDTO):
    id: Optional[UUID] = None


class ProfileSetup(BaseModel):
    id: Optional[UUID] = None
    name: str
    dob: datetime
    gender: Gender
    role: Optional[Literal["owner", "caretaker"]] = None
