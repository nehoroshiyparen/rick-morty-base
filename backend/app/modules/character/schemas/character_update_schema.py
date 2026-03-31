from pydantic import BaseModel
from typing import Optional
from app.infrastructure.integrations.rick_morty.schemas import StatusEnum, GenderEnum

class CharacterUpdateSchema(BaseModel):
    name: Optional[str] = None
    status: Optional[StatusEnum] = None
    species: Optional[str] = None
    type: Optional[str] = None
    gender: Optional[GenderEnum] = None