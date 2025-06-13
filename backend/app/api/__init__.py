from fastapi import APIRouter
from .confess import router as confess_router
from .instagram import router as instagram_router

# Create main router
router = APIRouter()

# Include confess router with prefix
router.include_router(confess_router, prefix="/confess", tags=['confessions'])
router.include_router(instagram_router, prefix="/instagram", tags=['Instagram'])