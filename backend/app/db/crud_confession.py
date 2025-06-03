# All create, read, update and delete functions for confession related DB data

from sqlalchemy.orm import Session
from app.models.confession import Confession
from app.services.gemini_client import model
from app.db.session import SessionLocal

def create_confession(db: Session, content: str):
    confession = Confession(content=content, published=False)
    db.add(confession)
    db.commit()
    db.refresh(confession) # Get ID after insertion
    return confession



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
    generate_confessions()
