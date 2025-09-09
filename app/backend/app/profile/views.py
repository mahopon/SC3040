from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from app.database.core import DbSession
from app.auth.dependency import get_id_from_session
from .service import initial_setup_profile
from .schemas import ProfileSetup
from .enums import Role
from uuid import UUID

profile_router = APIRouter()


@profile_router.put("/setup")
def setup_profile(
    db_session: DbSession, profile: ProfileSetup, profile_id: UUID = Depends(get_id_from_session)
) -> Response:
    profile.id = profile_id
    print(profile_id)
    initial_setup_profile(db_session=db_session, profile=profile)
    if profile.role == Role.PetOwner.value:
        # TODO Add petowner row creation
        pass
    elif profile.role == Role.PetCareTaker.value:
        # TODO Add petcaretaker row creation
        pass
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@profile_router.patch("/update")
def update_profile(
    db_session: DbSession, profile: ProfileSetup, profile_id: UUID = Depends(get_id_from_session)
) -> Response:
    pass
