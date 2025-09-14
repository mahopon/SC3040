from app.auth.exception_handlers import (
    invalid_credentials_exception_handler,
    email_exists_exception_handler,
    password_mismatch_exception_handler,
)
from app.auth.exceptions import InvalidCredentials, EmailAlreadyExists, PasswordMismatch

from fastapi import FastAPI, status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    msg = str(exc.errors()[0]["msg"])
    msg = msg.removeprefix("Value error, ")
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content={"message": msg})


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(InvalidCredentials, invalid_credentials_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(EmailAlreadyExists, email_exists_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(PasswordMismatch, password_mismatch_exception_handler)  # type: ignore[arg-type]
    app.add_exception_handler(RequestValidationError, validation_exception_handler)  # type: ignore[arg-type]
