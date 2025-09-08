from pydantic import BaseModel, SecretStr, field_validator
from datetime import datetime
from uuid import UUID
from typing import Optional
from .models import Auth


class AuthLogin(BaseModel):
    email: str
    password: SecretStr

    @field_validator("password")
    def validate_password(cls, v: SecretStr):
        pw = v.get_secret_value()
        if len(pw) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.islower() for c in pw):
            raise ValueError("Password must contain a lowercase letter")
        if not any(c.isupper() for c in pw):
            raise ValueError("Password must contain an uppercase letter")
        if not any(c.isdigit() for c in pw):
            raise ValueError("Password must contain a digit")
        if not any(c in "@$!%*?&" for c in pw):
            raise ValueError("Password must contain a special character (@$!%*?&)")
        return v


class AuthRegister(AuthLogin):
    name: str
    dob: datetime


class AuthLoginResponse(BaseModel):
    user_id: UUID
    name: str
    token: str


class AuthRegisterResponse(BaseModel):
    message: str


class AuthRead(BaseModel):
    pass


class AuthUpdate(BaseModel):
    pass


class AuthPasswordUpdate(BaseModel):
    old_password: SecretStr
    new_password: SecretStr

    @field_validator("new_password")
    def validate_password(cls, v: SecretStr):
        pw = v.get_secret_value()
        if len(pw) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.islower() for c in pw):
            raise ValueError("Password must contain a lowercase letter")
        if not any(c.isupper() for c in pw):
            raise ValueError("Password must contain an uppercase letter")
        if not any(c.isdigit() for c in pw):
            raise ValueError("Password must contain a digit")
        if not any(c in "@$!%*?&" for c in pw):
            raise ValueError("Password must contain a special character (@$!%*?&)")
        return v


class OAuthRegister(AuthLogin):
    name: str


class OAuthOutcome(BaseModel):
    existing_auth: Optional[Auth] = None  # type: ignore # noqa
    registration: Optional[OAuthRegister] = None

    model_config = {"arbitrary_types_allowed": True}


class OAuthProvider(BaseModel):
    name: str
    client_id: str
    client_secret: str
    access_token_url: str
    authorize_url: str
    api_base_url: str
    server_metadata_url: str
    client_kwargs: Optional[dict[str, str]] = {}
