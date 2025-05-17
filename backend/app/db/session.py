from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://naveed@localhost:5432/confessions_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    # Connect to DB
    db = SessionLocal()
    try:
        # Let user use DB (passed into API route)
        yield db
    finally:
        # Close session after request is complete
        db.close()