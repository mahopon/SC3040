from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from .dependency import InternalProfileSvc as ProfileSvc
from app.auth.dependency import CurrentId
from fastapi.responses import JSONResponse, Response
from .schemas import (
    ProfileUpdate,
    ProfileCareTakerUpdate,
    ProfileInitialUpdate,
    ProfileInitialUpdateRequest,
    ProfileOwnerUpdate,
)
from app.petowner.dependency import ExternalPetOwnerSvc as PetOwnerSvc
from app.petowner.schemas import PetOwnerCreate
from app.petcaretaker.dependency import ExternalPetCareTakerSvc as PetCareTakerSvc
from app.petcaretaker.schemas import PetCareTakerCreate, PetCareTakerUpdate
from app.pet.dependency import ExternalPetSvc as PetSvc
from .enums import Role
from fastapi.exceptions import HTTPException

profile_router = APIRouter()


@profile_router.get("")
def get_profile(id: CurrentId, profile_service: ProfileSvc) -> JSONResponse:
    profile = profile_service.get_profile(profile_id=id)
    content = jsonable_encoder(profile.model_dump(exclude_none=True))
    return JSONResponse(status_code=status.HTTP_200_OK, content=content)


@profile_router.put("/initial")
def onboard_profile(
    id: CurrentId,
    profile_service: ProfileSvc,
    profile_update_req: ProfileInitialUpdateRequest,
    petowner_service: PetOwnerSvc,
    petcaretaker_service: PetCareTakerSvc,
    pet_service: PetSvc,
) -> Response:
    profile_update = ProfileInitialUpdate(**profile_update_req.model_dump(exclude={"yoe", "pet"}))
    profile_service.initial_update_profile(profile_id=id, profile_update=profile_update)
    # Add row based on role
    if profile_update_req.type == Role.PetOwner.value:
        if not profile_update_req.pet:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No pet provided")
        new_petowner = PetOwnerCreate(id=id)
        petowner_service.create_pet_owner(petowner_new=new_petowner)
        pet_service.create_pet(owner_id=id, pet_new=profile_update_req.pet)
    elif profile_update_req.type == Role.PetCareTaker.value:
        if not profile_update_req.yoe:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="No years of experience(yoe) provided"
            )
        new_petcaretaker = PetCareTakerCreate(id=id, yoe=profile_update_req.yoe)
        petcaretaker_service.create_petcaretaker(petcaretaker_new=new_petcaretaker)
    return Response(status_code=status.HTTP_200_OK)


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
