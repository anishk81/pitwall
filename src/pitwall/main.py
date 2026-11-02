from fastapi import FastAPI

from pitwall.api.routes import health
from pitwall.config import get_settings


def create_app() -> FastAPI:
    """App factory: builds a fresh, fully configured app."""
    settings = get_settings()
    app = FastAPI(title=settings.app_name, version="0.1.0")
    app.include_router(health.router)
    return app


app = create_app()