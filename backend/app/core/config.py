from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path
from typing import List

class Settings(BaseSettings):

    DATABASE_URL: str

    OPENAI_API_KEY: str = ""

    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    UPLOAD_DIR: Path = Path("uploads")

    ALLOWED_CONTENT_TYPES: set[str] = {
        "text/plain",
        "application/pdf",
        "text/markdown",
    }

    CORS_ORIGINS: List[str] = [
        "http://localhost:5173"
    ]

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()