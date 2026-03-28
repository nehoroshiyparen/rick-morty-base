from app.core.config import settings
from .engine import create_async_engine

engine = create_async_engine(settings.DATABASE_URL)