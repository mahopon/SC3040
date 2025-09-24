from app.auth.exception_handlers import (
    invalid_credentials_exception_handler,
    email_exists_exception_handler,
    password_mismatch_exception_handler,
)
from app.auth.exceptions import InvalidCredentials, EmailAlreadyExists, PasswordMismatch
from app.profile.exception_handlers import (
    profile_exists_exception_handler,
    profile_not_exists_exception_handler,
    profile_onboarded_exception_handler,
)
from app.profile.exceptions import ProfileAlreadyExists, ProfileAlreadyOnboarded, ProfileNotExists
from app.petcaretaker.exception_handlers import petcaretaker_not_found_exception_handler
from app.petcaretaker.exceptions import PetCareTakerNotFound
from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    msg = str(exc.errors()[0]["msg"])
    msg = msg.removeprefix("Value error, ")
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"message": msg})


def register_exception_handlers(app: FastAPI) -> None:
    # Global
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]
    # Auth
    app.add_exception_handler(InvalidCredentials, invalid_credentials_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(EmailAlreadyExists, email_exists_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(PasswordMismatch, password_mismatch_exception_handler)  # type: ignore[arg-type]
    # Profile
    app.add_exception_handler(ProfileNotExists, profile_not_exists_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(ProfileAlreadyOnboarded, profile_onboarded_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(ProfileAlreadyExists, profile_exists_exception_handler)  # type: ignore[arg-type]
    # PetCareTaker
    app.add_exception_handler(PetCareTakerNotFound, petcaretaker_not_found_exception_handler)  # type: ignore[arg-type]
