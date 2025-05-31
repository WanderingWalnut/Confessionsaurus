from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from ..models import confession as models
from ..schemas import confession as schemas
from ..db.session import get_db

router = APIRouter()

@router.post("/submit")
def submit_confession(confession: schemas.ConfessionBase, db: Session = Depends(get_db)):
    try:
        # Create a new db model insatnce
        db_confession = models.Confession(
            content=confession.content
        )

        # Add the new row to the db
        db.add(db_confession)

        # Save the changes
        db.commit()

        # Refresh the instance to get auto-generated fields
        db.refresh(db_confession)

        return{
            "Status": "Success",
            "Message": "Confession created successfully",
            "data": {
                "id": db_confession.id,
                "content": db_confession.content,
                "published": db_confession.published,
                "created_at": db_confession.created_at
            }
        }

    except Exception as e:
        # If anything goes wrong, roll back the DB to previous state
        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=f"An error occured while creating the confession: {str(e)}"
        )

@router.get("/confessions")
def get_confession(db: Session = Depends(get_db)):
    try:
        confession = db.query(models.Confession).filter(models.Confession.published == False).first()
        
        if not confession:
            raise HTTPException(
                status_code=404,
                detail="No unpublished confessions available"
            )

        # Mark as published instead of deleting
        confession.published = True
        db.commit()
        
        return {
            "status": "success",
            "message": "Confession retrieved and marked as published",
            "data": {
                "id": confession.id,
                "content": confession.content,
                "published": confession.published,
                "created_at": confession.created_at
            }
        }
    
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error occurred: {str(e)}"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred: {str(e)}"
        )

    