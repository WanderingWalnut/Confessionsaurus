from fastapi import APIRouter

router = APIRouter()

@router.post("/admin/approve")
def approve_confession():
    return {"message": "Confession approved"}

@router.post("/admin/reject")
def reject_confession():
    return {"message": "Confession rejected"} 