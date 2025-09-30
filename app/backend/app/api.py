from fastapi import APIRouter
from app.auth.views import auth_router
from app.profile.views import profile_router
from app.onboarding.views import onboarding_router
from app.service.views import service_router, offered_service_router
from app.location.views import location_router

router = APIRouter()

# Include all views/routes here from individual domains
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(profile_router, prefix="/profile", tags=["Profile"])
router.include_router(onboarding_router, prefix="/onboarding", tags=["Onboarding"])
router.include_router(service_router, prefix="/service", tags=["Service"])
router.include_router(offered_service_router, prefix="/offered-service", tags=["Offered Service"])
router.include_router(location_router, prefix="/location", tags=["Location"])
