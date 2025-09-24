from .protocols import InternalProfileService
from .repository import ProfileRepository
from .schemas import (
    ProfileAuthRegister,
    Profile as ProfileDTO,
    ProfileOAuthRegister,
    ProfileUpdate,
    ProfileInitialUpdate,
)

from .models import Profile
from uuid import UUID
from .exceptions import ProfileAlreadyExists, ProfileNotExists, ProfileAlreadyOnboarded


class ProfileService(InternalProfileService):
    def __init__(self, repo: ProfileRepository):
        self.repo = repo

    def register_profile(self, *, profile_id: UUID, profile_new: ProfileAuthRegister) -> None:
        if self.repo.get_by_id(profile_id):
            raise ProfileAlreadyExists("Profile already exists")
        profile = Profile(**profile_new.model_dump(exclude_unset=True, exclude={"yoe"}))
        profile.id = profile_id
        self.repo.create_profile(profile_new=profile)

    def get_profile(self, *, profile_id: UUID) -> ProfileDTO:
        profile = self.repo.get_by_id(profile_id=profile_id)
        if not profile:
            raise ProfileNotExists("Profile doesn't exist")
        return_profile = ProfileDTO.model_validate(profile)
        if profile.type == "caretaker" and hasattr(profile, "petcaretaker"):
            return_profile.yoe = profile.petcaretaker.yoe
        return return_profile

    def oauth_process_profile(self, *, profile_id: UUID, profile_new: ProfileOAuthRegister) -> None:
        profile = self.repo.get_by_id(profile_id=profile_id)
        if profile:
            return
        self._oauth_register_profile(profile_id=profile_id, profile_new=profile_new)

    def _oauth_register_profile(self, *, profile_id: UUID, profile_new: ProfileOAuthRegister) -> None:
        profile = Profile(**profile_new.model_dump(exclude_unset=True, exclude={"yoe"}))
        profile.id = profile_id
        self.repo.create_profile(profile_new=profile)

    def initial_update_profile(self, *, profile_id: UUID, profile_update: ProfileInitialUpdate) -> None:
        profile = self.repo.get_by_id(profile_id=profile_id)
        if not profile:
            raise ProfileNotExists("Profile doesn't exist")
        if profile.setup:
            raise ProfileAlreadyOnboarded("Profile has already completed onboarding")
        self.repo.onboard_profile(profile_id=profile.id, profile_update=profile_update)

    def update_profile(self, *, profile_id: UUID, profile_update: ProfileUpdate) -> None:
        profile = self.repo.get_by_id(profile_id)
        if not profile:
            raise ProfileNotExists("Profile doesn't exist")
        self.repo.update_profile(profile_id=profile.id, profile_update=profile_update)
