from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.init_db import init_db
from app.core.middleware import register_middlewares
from app.core.rate_limit import register_rate_limit

from app.api.v1.admin import router as admin_router
from app.api.v1.auth import router as auth_router
from app.api.v1.chat import router as chat_router
from app.api.v1.conversations import router as conversations_router
from app.api.v1.files import router as files_router
from app.api.v1.health import router as health_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

register_middlewares(app)
register_rate_limit(app)
app.include_router(admin_router)
app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(files_router)
app.include_router(conversations_router)
app.include_router(health_router)
