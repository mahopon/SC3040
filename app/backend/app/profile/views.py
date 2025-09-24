from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from .dependency import InternalProfileSvc as ProfileSvc
from app.auth.dependency import CurrentId
from fastapi.responses import JSONResponse, Response
from .schemas import (
    ProfileUpdate,
    ProfileCareTakerUpdate,
    ProfileOwnerUpdate,
)
from app.petcaretaker.dependency import ExternalPetCareTakerSvc as PetCareTakerSvc
from app.petcaretaker.schemas import PetCareTakerUpdate

profile_router = APIRouter()


@profile_router.get("")
def get_profile(id: CurrentId, profile_service: ProfileSvc) -> JSONResponse:
    profile = profile_service.get_profile(profile_id=id)
    content = jsonable_encoder(profile.model_dump(exclude_none=True))
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


@profile_router.patch("/caretaker")
def update_caretaker_profile(
    id: CurrentId,
    profile_service: ProfileSvc,
    petcaretaker_service: PetCareTakerSvc,
    profile_update_req: ProfileCareTakerUpdate,
) -> Response:
    profile_full_update = profile_update_req.model_dump()
    profile_update_cols = list(ProfileUpdate.model_fields.keys())
    profile_caretaker_cols = [key for key in profile_update_cols if key not in profile_update_cols]
    profile_update = {key: profile_full_update[key] for key in profile_update_cols}
    profile_caretaker_update = {key: profile_full_update[key] for key in profile_caretaker_cols}
    profile_service.update_profile(profile_id=id, profile_update=ProfileUpdate(**profile_update))
    if profile_caretaker_update["yoe"] is not None:
        petcaretaker_service.update_petcaretaker(
            petcaretaker_id=id, petcaretaker_update=PetCareTakerUpdate(**profile_caretaker_update)
        )
    return Response(status_code=status.HTTP_200_OK)


@profile_router.patch("/owner")
def update_owner_profile(
    id: CurrentId, profile_service: ProfileSvc, profile_update_req: ProfileOwnerUpdate
) -> Response:
    profile_update = ProfileUpdate(**profile_update_req.model_dump())
    profile_service.update_profile(profile_id=id, profile_update=profile_update)
    return Response(status_code=status.HTTP_200_OK)
