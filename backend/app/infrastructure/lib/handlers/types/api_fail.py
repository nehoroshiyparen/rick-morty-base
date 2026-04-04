from pydantic import BaseModel
from typing import Optional

class ApiFail(BaseModel):
    success: bool = False
    error: str
    status: Optional[int] = None