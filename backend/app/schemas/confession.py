from pydantic import BaseModel, Field

class ConfessionBase(BaseModel):
    # Len of confession, min and max
    content: str = Field(..., min_length=1, max_length=1000)

class ConfessionCreate(ConfessionBase):
    pass

class ConfessionOut(ConfessionBase):
    id: int

    class Config:
        orm_mode = True 