from .repository import LocationRepository
from .service import LocationService
from .protocols import InternalLocationService
from app.database.core import DbSession
from fastapi import Depends
from typing import Annotated


async def get_location_repo(db_session: DbSession) -> LocationRepository:
    return LocationRepository(db_session=db_session)


async def get_location_service(repo: LocationRepository = Depends(get_location_repo)) -> LocationService:
    return LocationService(repo=repo)


InternalLocationSvc = Annotated[InternalLocationService, Depends(get_location_service)]
