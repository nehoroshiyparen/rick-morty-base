from pydantic import BaseModel, HttpUrl
from typing import List
from datetime import datetime


class EpisodeSchema(BaseModel):
    id: int
    name: str

    air_date: str 
    episode: str 

    characters: List[HttpUrl]

    url: HttpUrl
    created: datetime