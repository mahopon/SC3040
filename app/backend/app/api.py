from fastapi import APIRouter
from app.auth.views import auth_router
from app.profile.views import profile_router
from app.onboarding.views import onboarding_router
from app.service.views import service_router

router = APIRouter()

# Include all views/routes here from individual domains
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(profile_router, prefix="/profile", tags=["Profile"])
router.include_router(onboarding_router, prefix="/onboarding", tags=["Onboarding"])
router.include_router(service_router, prefix="/service", tags=["Service"])
