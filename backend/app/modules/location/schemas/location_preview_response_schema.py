from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class LocationPreviewResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    external_id: int
    name: str
    dimension: str