from pydantic import BaseModel

class ConfessionBase(BaseModel):
    content: str

class ConfessionCreate(ConfessionBase):
    pass

class ConfessionOut(ConfessionBase):
    id: int

    class Config:
        orm_mode = True 