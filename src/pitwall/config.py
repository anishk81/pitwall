from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App configuration, read from environment variables and .env.

    Field names map to env vars case-insensitively:
    groq_api_key <- GROQ_API_KEY
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore unrelated vars in .env
    )

    app_name: str = "Pitwall"
    environment: Literal["local", "test", "prod"] = "local"
    log_level: str = "INFO"

    # Infrastructure (Docker Compose will provide these)
    database_url: str = "postgresql+psycopg://pitwall:pitwall@localhost:5432/pitwall"
    redis_url: str = "redis://localhost:6379/0"

    # LLM providers (filled in Task 2)
    groq_api_key: SecretStr | None = None
    gemini_api_key: SecretStr | None = None
    ollama_base_url: str = "http://localhost:11434"


@lru_cache
def get_settings() -> Settings:
    """Build Settings once and reuse it (a cached singleton)."""
    return Settings()