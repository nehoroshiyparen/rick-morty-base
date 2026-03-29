from app.infrastructure.database import BaseRepository
from .models import Location

class LocationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Location)