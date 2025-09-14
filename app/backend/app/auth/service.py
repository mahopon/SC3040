from .models import Auth, AuthSession
from .schemas import AuthRegister, AuthPasswordUpdate, OAuthOutcome, OAuthRegister
from .repository import AuthRepository
from uuid import UUID
from authlib.integrations.starlette_client import OAuth
from fastapi.requests import Request
from .exceptions import InvalidCredentials, EmailAlreadyExists, PasswordMismatch
from .protocols import InternalAuthService


class AuthService(InternalAuthService):
    def __init__(self, repo: AuthRepository):
        self.repo = repo

    def login(self, *, email: str, password: str) -> Auth:
        auth = self.repo.get_by_email(email)
        if auth is None:
            raise InvalidCredentials("Invalid credentials")

        if not auth.verify_password(password):
            raise InvalidCredentials("Invalid credentials")

        return auth

    def retrieve_auth_by_session(self, *, session_id: str) -> Auth:
        auth = self.repo.get_by_session_id(session_id)
        if auth is None:
            raise InvalidCredentials("Session doesn't exist")
        return auth

    def register_web(self, *, auth_in: AuthRegister) -> Auth:
        email = auth_in.email
        auth = self.repo.get_by_email(email)
        if auth:
            raise EmailAlreadyExists("Email is already in use")
        new_auth = Auth(**auth_in.model_dump(exclude={"password", "name", "dob", "gender"}))
        if auth_in.password:
            new_auth.set_password(auth_in.password.get_secret_value())
        self.repo.create_auth(new_auth)
        return new_auth

    def register_oauth(self, *, auth_in: OAuthRegister) -> Auth:
        new_auth = Auth(**auth_in.model_dump(exclude={"name"}))
        self.repo.create_auth(new_auth)
        return new_auth

    def create_session(self, *, auth: Auth) -> AuthSession:
        session = AuthSession(auth=auth, session_id=auth.token)
        self.repo.create_session(session)
        return session

    def change_password(self, *, user_id: UUID, auth_pw_in: AuthPasswordUpdate) -> None:
        auth = self.repo.get_by_id(user_id)
        if auth is None:
            raise InvalidCredentials("User does not exist")

        if auth.password is None:
            auth.set_password(auth_pw_in.new_password.get_secret_value())
            return

        if not auth.verify_password(auth_pw_in.old_password.get_secret_value()):
            raise PasswordMismatch("Invalid old password")

        auth.set_password(auth_pw_in.new_password.get_secret_value())

    async def process_oauth_callback(self, oauth: OAuth, request: Request) -> OAuthOutcome:
        token = await oauth.google.authorize_access_token(request)
        email = token["userinfo"]["email"]
        name = token["userinfo"]["name"]
        auth = self.repo.get_by_email(email)
        if auth:
            return OAuthOutcome(existing_auth=auth)
        return OAuthOutcome(registration=OAuthRegister(email=email, name=name))
