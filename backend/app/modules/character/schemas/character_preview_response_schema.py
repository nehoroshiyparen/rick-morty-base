from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.modules.character.models.character import Status, Gender

class CharacterPreviewResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True) 

    id: int
    external_id: int
    name: str
    status: Status
    image: str