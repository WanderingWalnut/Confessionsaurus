from pydantic import BaseModel, Field
from ..models.confession import ConfessionStatus

class ConfessionBase(BaseModel):
    # Len of confession, min and max
    content: str = Field(..., min_length=1, max_length=1000)

class ConfessionCreate(ConfessionBase):
    pass

class ConfessionOut(ConfessionBase):
    id: int
    status: ConfessionStatus
    published: bool
    created_at: str

    class Config:
        orm_mode = True 