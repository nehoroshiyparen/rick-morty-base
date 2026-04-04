from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime
from app.modules.character.schemas.character_preview_response_schema import CharacterPreviewResponseSchema

class LocationFullResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    type: Optional[str]
    dimension: str
    url: str
    created_at: Optional[datetime]
    characters_location: List[CharacterPreviewResponseSchema]