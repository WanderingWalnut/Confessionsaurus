# Placeholder for SQLAlchemy confession model
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Confession(Base):
    __tablename__ = "confessions"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))