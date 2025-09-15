from pydantic import BaseModel, SecretStr, field_validator, StringConstraints, EmailStr
from datetime import datetime, timezone
from typing import Optional, Annotated
from app.profile.enums import Gender


class AuthLogin(BaseModel):
    email: EmailStr
    password: SecretStr

    @field_validator("password")
    def validate_password(cls, v: SecretStr) -> SecretStr:
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
    name: Annotated[str, StringConstraints(min_length=3)]
    dob: datetime
    gender: Gender

    @field_validator("dob")
    def validate_dob(cls, v: datetime) -> datetime:
        if v.date() >= datetime.now(timezone.utc).date():
            raise ValueError("Date of Birth cannot be today or later")
        return v


class AuthLoginResponse(BaseModel):
    session_id: str


class AuthPasswordUpdate(BaseModel):
    old_password: SecretStr
    new_password: SecretStr

    @field_validator("new_password")
    def validate_password(cls, v: SecretStr) -> SecretStr:
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


class OAuthRegister(BaseModel):
    email: str
    name: str


class OAuthLoginResponse(AuthLoginResponse):
    pass


class OAuthProvider(BaseModel):
    name: str
    client_id: str
    client_secret: str
    access_token_url: str
    authorize_url: str
    api_base_url: str
    server_metadata_url: str
    client_kwargs: Optional[dict[str, str]] = {}
