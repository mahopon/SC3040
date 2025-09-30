from .protocols import InternalLocationService
from .repository import LocationRepository
from typing import List
from .schemas import Location as LocationDTO


class LocationService(InternalLocationService):
    """
    Service for retrieving locations from the repository and converting them to DTOs.

    Args:
        repo (LocationRepository): Repository instance for accessing location data.
    """

    def __init__(self, repo: LocationRepository):
        self.repo = repo

    def get_locations(self) -> List[LocationDTO]:
        """
        Get all locations as a list of DTOs.

        Returns:
            List[LocationDTO]: List of location data transfer objects.
        """
        all_locations = self.repo.get_all_locations()
        return [LocationDTO.model_validate(location) for location in all_locations]
