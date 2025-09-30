from pydantic import BaseModel
from typing import List
from .enums import Day


class Service(BaseModel):
    """
    Pydantic schema representing a service.
    """

    id: int
    name: str

    model_config = {"from_attributes": True}


class OfferedService(BaseModel):
    """
    Pydantic schema representing an offered service by a caretaker.
    """

    id: int
    name: str
    rate: int


class OfferedServiceCreate(BaseModel):
    """
    Schema for creating a new OfferedService.
    """

    service_id: int
    rate: int
    day: List[Day]


class OfferedServiceUpdate(BaseModel):
    rate: int
    day: List[Day]
