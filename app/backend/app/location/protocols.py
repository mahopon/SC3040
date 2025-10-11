from typing import Protocol, List
from .schemas import Location as LocationDTO


class ExternalLocationService(Protocol):
    def get_filtered_locations(self, *, location_ids: List[int]) -> List[LocationDTO]: ...


class InternalLocationService(ExternalLocationService, Protocol):
    """
    Protocol for internal-facing location service.
    """

    def get_locations(self) -> List[LocationDTO]: ...
