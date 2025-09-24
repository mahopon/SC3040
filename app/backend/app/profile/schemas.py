from pydantic import BaseModel, StringConstraints, field_validator
from typing import Optional, Literal, Annotated
from datetime import datetime
from .enums import Gender
from app.pet.schemas import PetCreate


class Profile(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    dob: Optional[datetime] = None
    gender: Optional[Gender] = None
    contact_num: Optional[str] = None
    address: Optional[str] = None
    type: Optional[str] = None
    yoe: Optional[int] = None

    class Config:
        from_attributes = True


class ProfileAuthRegister(Profile):
    pass


class ProfileUpdate(BaseModel):
    first_name: Optional[Annotated[str, StringConstraints(min_length=3)]] = None
    last_name: Optional[Annotated[str, StringConstraints(min_length=3)]] = None
    contact_num: Optional[str] = None
    address: Optional[str] = None


class ProfileCareTakerUpdate(ProfileUpdate):
    yoe: Optional[str] = None

    @field_validator("yoe")
    def yoe_gt_zero(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Years of experience(yoe) must be greater or equal to 0")
        return value


class ProfileOwnerUpdate(ProfileUpdate):
    pass


class ProfileOAuthRegister(ProfileAuthRegister):
    pass


class ProfileInitialUpdateRequest(BaseModel):
    first_name: str
    last_name: str
    dob: datetime
    gender: Gender
    contact_num: str
    address: str
    type: Literal["owner", "caretaker"]
    yoe: Optional[int] = None
    pet: Optional[PetCreate] = None


class ProfileInitialUpdate(BaseModel):
    first_name: str
    last_name: str
    dob: datetime
    gender: Gender
    contact_num: str
    address: str
    type: Literal["owner", "caretaker"]
