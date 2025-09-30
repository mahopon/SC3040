from typing import Protocol, List
from .schemas import Location as LocationDTO


class InternalLocationService(Protocol):
    """
    Protocol for internal-facing location service.
    """

    def get_locations(self) -> List[LocationDTO]: ...
