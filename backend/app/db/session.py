from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# load_dotenv()  # Commented out for Lambda - env vars set in AWS console
# NEON_TECH_DB_URL = os.getenv("NEON_TECH_DB_URL")  # Commented out for Lambda
NEON_TECH_DB_URL = os.environ['NEON_TECH_DB_URL']  # Lambda-compatible

engine = create_engine(
    NEON_TECH_DB_URL,            # keep using psycopg2/psycopg
    pool_pre_ping=True,          # “SELECT 1” before giving a conn
    pool_recycle=300,            # drop anything >5 min old
    pool_size=5,                 # tiny pool for Lambda
    max_overflow=0,              # don’t create unpooled extras
)
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