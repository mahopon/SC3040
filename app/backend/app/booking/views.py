from fastapi import APIRouter, status, Path
from fastapi.responses import JSONResponse
from app.auth.dependency import CurrentId
from .schemas import BookingCreate

booking_router = APIRouter()


@booking_router.get("")
def get_bookings(id: CurrentId) -> JSONResponse:
    return JSONResponse(status_code=status.HTTP_200_OK, content={})


@booking_router.get("/{booking_id}")
def get_booking_details(booking_id: int = Path(...)) -> JSONResponse:
    pass


@booking_router.post("/create")
def create_booking(booking_details: BookingCreate):
    pass


@booking_router.put("/{booking_id}/accept")
def accept_booking(id: CurrentId, booking_id: int = Path(...)):
    pass


@booking_router.put("/{booking_id}/decline")
def decline_booking(id: CurrentId, booking_id: int = Path(...)):
    pass


@booking_router.put("/{booking_id}/cancel")
def cancel_booking(id: CurrentId, booking_id: int = Path(...)):
    pass
