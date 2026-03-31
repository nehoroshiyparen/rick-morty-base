from pydantic import BaseModel
from typing import Optional

class EpisodeUpdateSchema(BaseModel):
    name: Optional[str] = None