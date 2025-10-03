from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from app.auth.dependency import CurrentId

booking_router = APIRouter()


@booking_router.get("")
def get_bookings(id: CurrentId) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content={})
