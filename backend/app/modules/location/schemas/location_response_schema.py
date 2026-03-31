from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LocationResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    type: Optional[str]
    dimension: str
    url: str
    created_at: Optional[datetime]