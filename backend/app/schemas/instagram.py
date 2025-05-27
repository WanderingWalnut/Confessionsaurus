from pydantic import BaseModel

class InstagramPostRequest(BaseModel):
    image_path: str
    caption: str