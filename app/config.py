# app/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # JWT
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_MINUTES: int = 60

    # Storage backend (local or s3)
    STORAGE_BACKEND: str = "local"

    # LLM provider (llama or openai)
    LLM_PROVIDER: str = "llama"

    # Optional: paths, API keys, etc.
    MODEL_PATH: str | None = None
    S3_BUCKET: str | None = None

    class Config:
        env_file = ".env"   # tells Pydantic to load values from .env

# Create a global settings instance
settings = Settings()

