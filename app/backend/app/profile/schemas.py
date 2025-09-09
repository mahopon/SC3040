from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Literal
from datetime import datetime
from .enums import Gender


class ProfileRegister(BaseModel):
    name: str
    dob: Optional[datetime] = None
    gender: Optional[Gender] = None


class ProfileSetup(BaseModel):
    id: Optional[UUID] = None
    name: str
    dob: datetime
    gender: Gender
    role: Literal["owner", "caretaker"]
