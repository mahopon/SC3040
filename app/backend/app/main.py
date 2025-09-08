from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import router
from starlette.middleware.sessions import SessionMiddleware
import uvicorn
from contextlib import asynccontextmanager
from app.config import get_settings
from typing import AsyncGenerator
from secrets import token_urlsafe

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    yield


app = FastAPI(title=settings.APP_NAME, docs_url="/docs", lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, token_urlsafe(32))

app.include_router(router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Welcome to PawfectMatch"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
