from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class EpisodePreviewResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    air_date: Optional[datetime]
    episode: str