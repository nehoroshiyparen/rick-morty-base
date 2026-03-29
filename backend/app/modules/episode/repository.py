from  app.infrastructure.database import BaseRepository
from .models import Episode

class EpisodeRepository(BaseRepository):
    def __init__(self):
        super().__init__(Episode)