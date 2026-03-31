from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class EpisodeResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    air_date: Optional[datetime]
    episode: str
    url: str
    created_at: Optional[datetime]