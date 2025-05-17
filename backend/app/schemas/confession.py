from pydantic import BaseModel
from typing import Optional

class ConfessionBase(BaseModel):
    content: str
    category: Optional[str] = None
    is_anonymous: bool = True

class ConfessionCreate(ConfessionBase):
    pass

class ConfessionOut(ConfessionBase):
    id: int

    class Config:
        orm_mode = True 