from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime


class LocationSchema(BaseModel):
    id: int
    name: str
    type: Optional[str] = None
    dimension: Optional[str] = None

    residents: List[HttpUrl]

    url: HttpUrl
    created: datetime