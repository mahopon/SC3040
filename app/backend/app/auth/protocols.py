from .schemas import (
    AuthRegister,
    AuthPasswordUpdate,
    OAuthLoginResponse,
    OAuthRegister,
    AuthLoginResponse,
    AuthRegisterResponse as AuthDTO,
)
from .models import Auth, AuthSession
from uuid import UUID
from authlib.integrations.starlette_client import OAuth
from fastapi.requests import Request
from typing import Protocol
from pydantic import SecretStr


class InternalAuthService(Protocol):
    def login(self, *, email: str, password: SecretStr) -> AuthLoginResponse: ...

    def retrieve_auth_id_by_session(self, *, session_id: str) -> UUID: ...

    def register(self, *, auth_in: AuthRegister) -> AuthDTO: ...

    def _register_oauth(self, *, auth_in: OAuthRegister) -> Auth: ...

    def _create_session(self, *, auth: Auth) -> AuthSession: ...

    def change_password(self, *, user_id: UUID, auth_pw_in: AuthPasswordUpdate) -> None: ...

    async def process_oauth_callback(self, oauth: OAuth, request: Request) -> OAuthLoginResponse: ...
