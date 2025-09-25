from pydantic import BaseModel
from typing import List
from .enums import Day


class Service(BaseModel):
    """
    Pydantic schema representing a service.
    """

    id: int
    name: str


class OfferedService(Service):
    """
    Pydantic schema representing an offered service by a caretaker.
    """

    rate: int


class OfferedServiceCreate(BaseModel):
    """
    Schema for creating a new OfferedService.
    """

    service_id: int
    rate: int
    day: List[Day]
