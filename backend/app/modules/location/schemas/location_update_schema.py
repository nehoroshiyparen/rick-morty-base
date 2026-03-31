from pydantic import BaseModel
from typing import Optional

class LocationUpdateSchema(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    dimension: Optional [str] = None