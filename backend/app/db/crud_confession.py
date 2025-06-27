# All create, read, update and delete functions for confession related DB data

from sqlalchemy.orm import Session
from app.models.confession import Confession, ConfessionStatus
from app.services.gemini_client import model
from app.db.session import SessionLocal
from typing import Optional

def create_confession(db: Session, content: str):
    confession = Confession(content=content, published=False)
    db.add(confession)
    db.commit()
    db.refresh(confession) # Get ID after insertion
    return confession

def get_ready_confession(db: Session, n: int = 5):
    """ Grabs top n confessions that are READY """
    try:
        # Grab n confessions that are READY and OLDEST and return as a list
        confessions = db.query(Confession)\
            .filter(Confession.status == "READY")\
            .order_by(Confession.created_at.asc())\
            .limit(n)\
            .all()

        if not confessions:
            print("No confessions available")
            return []
        
        return confessions

    except Exception as e:
        print(f"Failed to read confessions: {str(e)}")
        return []
    
    finally:
        db.close()

def get_unmoderated_confessions(db: Session):
    """ Grab all "NEW" (unmoderated) confessions  """

    try:
        # Query DB to grab all confessions marked as "NEW"
        confessions = db.query(Confession)\
        .filter(Confession.status == "NEW")\
        .order_by(Confession.created_at.asc())\
        .all()

        # If no confessions exist
        if not confessions:
            print(f"No confessions available")
            return []

        return confessions
    
    except Exception as e:
        print(f"Error occurred while grabbing unmoderated confessions: {str(e)}")
        return []

def delete_confession(db: Session, confession_id: int):
    """ Deletes confession by specific ID """
    try:
        # First find the confession
        confession = db.query(Confession).filter(Confession.id == confession_id).first()
        if not confession:
            print(f"No confession found with ID {confession_id}")
            return False
            
        # Delete the specific confession
        db.delete(confession)
        db.commit()
        print(f"Confession with ID {confession_id} has been deleted")
        return True
    
    except Exception as e:
        db.rollback()
        print(f"Deleting confession failed: {str(e)}")
        return False
    
    finally:
        db.close()

def update_confession_to_posted(db: Session, confession: Confession):
    """" Updates confession to status POSTED"""

    try:
        # confession = db.query(Confession).filter(Confession.id == confession_id).first()

        if not confession:
            print(f"Confession with ID {confession.id} does not exist")
            return False
        
        confession.status = ConfessionStatus.posted # Use .value to get "POSTED" instead of "posted"
        db.commit()
        print(f"Successfully updated confession {confession.id} status to: {confession.status}")
        return confession
    
    except Exception as e:
        print(f"Failed to update confession status: {str(e)}")
        db.rollback()
        return False
    
    # Temp for testing run db.close(), in actual backend service main func will close session after all changes
    finally:
        db.close()

#TODO: Create function that can delete posted confessions, run as a scheduled job after creating func

def update_confession_status(db: Session, confession: Confession, confession_status: str, moderation_result_reason: Optional[str] = None):
    """ Updates confession status to READY """
    try:
        if not confession:
            print("Confession does not exist")
            return False
            
        confession.status = confession_status
        # If a reason exists update it i.e Pending confession
        if moderation_result_reason is not None:
            confession.reason = moderation_result_reason
            print(f"Confession is pending with following reason: {moderation_result_reason}")
        
        db.commit()  # Need to commit the changes
        print(f"Updated confession {confession.id} status to {confession_status}")
        return True
        
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"Failed to update confession status: {str(e)}")
        return False
        

def generate_confessions(n: int = 5):
    """ Function used to create 5 new confessions for testing"""
    prompt = f"""
    Generate {n} unique, human-like university confessions. 
    Each confession should be realistic, anonymous, and sound like something students would submit.
    Return only the confessions, separated by newline characters. 
    Do NOT number or label them. No extra text, only raw confessions.
    Do not say anything like "Okay, here are 5 university confessions".
    """

    response = model.generate_content(prompt)
    raw_text = response.text
    print("Raw Text: ", raw_text)
    
    # Split each confession into an item in a list and filter out empty strings
    confessions = [c.strip() for c in raw_text.split('\n') if c.strip()]
    print(f"Number of confessions after splitting: {len(confessions)}")
    print("Confessions list:", confessions)

    # Create an actual session instance
    db = SessionLocal()

    try:
        for confession in confessions:
            create_confession(db, confession)
        db.commit()
        print(f"Successfully created {len(confessions)} confessions")
    
    except Exception as e:
        db.rollback()
        print(f"Error occurred while creating confessions: {str(e)}")
    
    finally:
        db.close()

if __name__ == "__main__":
    # Create instance with skip_login=True to avoid Instagram login
    # session = InstagramSessionManager(skip_login=True)
    # Just generate 5 confessions
    # generate_confessions()

    db = SessionLocal()

    try:
        confession = db.query(Confession).first()
        print(f"Using following confession: {confession}")
        # Testing confession status updated
        update_confession_to_posted(db, confession)
    
    except Exception as e:
        print(f"Failed to fetch confession: {str(e)}")
