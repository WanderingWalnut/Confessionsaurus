from fastapi import APIRouter, HTTPException
from app.schemas import instagram as schemas
from app.services.instagram_poster import InstagramSessionManager
from pathlib import Path

router = APIRouter()
session = InstagramSessionManager()

@router.post('/post')
async def post_to_instagram(request: schemas.InstagramPostRequest):
    """ Posts pic & caption onto instagram """
    # Post photo
    try:
        result = session.post_photo(Path(request.image_path), request.caption)
        return {"status": "success", "post_id": result.id}
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail=str(e))


