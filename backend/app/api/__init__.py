from fastapi import APIRouter
from .confess import router as confess_router

# Create main router
router = APIRouter()

# Include confess router with prefix
router.include_router(confess_router, prefix="/confess", tags=['confessions'])