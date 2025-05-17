from fastapi import APIRouter

router = APIRouter()

@router.post("/confess")
def submit_confession():
    return {"message": "Confession submitted"}

@router.get("/confessions")
def list_confessions():
    return [] 