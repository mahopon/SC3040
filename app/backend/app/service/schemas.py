from pydantic import BaseModel
from typing import List
from .enums import Day


class Service(BaseModel):
    id: int
    name: str


class OfferedService(Service):
    rate: int


class OfferedServiceCreate(BaseModel):
    service_id: int
    rate: int
    day: List[Day]
