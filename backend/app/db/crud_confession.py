# All create, read, update and delete functions for confession related DB data

from sqlalchemy.orm import Session
from app.models import Confession

def create_confession(db: Session, content: str):
    confession = Confession(content=content, published=False)
    db.add(confession)
    db.commit()
    db.refresh(confession) # Get ID after insertion
    return confession

