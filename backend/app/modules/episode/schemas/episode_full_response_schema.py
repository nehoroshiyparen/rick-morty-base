from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.modules.character.schemas.character_preview_response_schema import CharacterPreviewResponseSchema

class EpisodeFullResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    air_date: Optional[datetime]
    episode: str
    url: str
    created_at: Optional[datetime]
    characters: List[CharacterPreviewResponseSchema]