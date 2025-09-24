from pydantic import BaseModel, field_validator
from uuid import UUID


class PetCareTaker(BaseModel):
    id: UUID
    yoe: int

    @field_validator("yoe")
    def yoe_gt_zero(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Years of Experience(yoe) must be 0 or greater")
        return value


class PetCareTakerCreate(PetCareTaker):
    pass


class PetCareTakerUpdate(BaseModel):
    yoe: int

    @field_validator("yoe")
    def yoe_gt_zero(cls, value: int) -> int:
        if value < 0:
            raise ValueError("Years of Experience(yoe) must be 0 or greater")
        return value
