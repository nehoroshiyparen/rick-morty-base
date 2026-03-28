from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    alive = "Alive"
    dead = "Dead"
    unknown = "unknown"


class GenderEnum(str, Enum):
    female = "Female"
    male = "Male"
    genderless = "Genderless"
    unknown = "unknown"

class LocationRef(BaseModel):
    name: str
    url: Optional[HttpUrl]  # иногда может быть пустая строка


class CharacterSchema(BaseModel):
    id: int
    name: str
    status: StatusEnum
    species: str
    type: Optional[str] = None
    gender: GenderEnum

    origin: LocationRef
    location: LocationRef

    image: HttpUrl
    episode: List[HttpUrl]

    url: HttpUrl
    created: datetime