from fastapi import APIRouter
from app.auth.views import auth_router
from app.profile.views import profile_router

router = APIRouter()

# Include all views/routes here from individual domains
router.include_router(auth_router, prefix="/auth", tags=["Auth"])
router.include_router(profile_router, prefix="/profile", tags=["Profile"])
