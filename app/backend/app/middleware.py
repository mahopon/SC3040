from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Any

EXCLUDE_PATHS = ["/", "/auth/login", "/auth/register", "/auth/login/google", "/docs", "/openapi.json"]


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Any) -> Any:
        if request.url.path in EXCLUDE_PATHS:
            return await call_next(request)

        # Auth check
        session_id = request.cookies.get("session_id")
        if not session_id:
            return JSONResponse({"detail": "Unauthorized"}, status_code=status.HTTP_401_UNAUTHORIZED)

        request.state.session_id = session_id
        return await call_next(request)
