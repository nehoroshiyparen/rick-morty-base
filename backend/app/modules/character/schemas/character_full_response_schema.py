from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.modules.character.models.character import Status, Gender
from app.modules.location.schemas.location_preview_response_schema import LocationPreviewResponseSchema
from app.modules.episode.schemas.episode_preview_response_schema import EpisodePreviewResponseSchema

class CharacterFullResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True) 

    id: int
    external_id: int
    name: str
    status: Status
    species: str
    type: Optional[str]
    gender: Gender
    image: str
    url: str
    created_at: Optional[datetime]
    origin: Optional[LocationPreviewResponseSchema]
    location: Optional[LocationPreviewResponseSchema]
    episodes: List[EpisodePreviewResponseSchema]