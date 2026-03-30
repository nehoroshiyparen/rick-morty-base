from pydantic import BaseModel, HttpUrl, field_validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

class StatusEnum(str, Enum):
    alive = "Alive"
    dead = "Dead"
    unknown = "Unknown"

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            normalized = value.strip().lower()
            mapping = {
                "alive": cls.alive,
                "dead": cls.dead,
                "unknown": cls.unknown,
            }
            return mapping.get(normalized)
        return None

class GenderEnum(str, Enum):
    female = "Female"
    male = "Male"
    genderless = "Genderless"
    unknown = "Unknown"

class LocationRef(BaseModel):
    name: str
    url: Optional[HttpUrl]

    @field_validator("url", mode="before")
    @classmethod
    def empty_string_to_none(cls, v):
        if v == "":
            return None
        return v


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