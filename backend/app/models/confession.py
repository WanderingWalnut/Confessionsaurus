# Placeholder for SQLAlchemy confession model
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Confession(Base):
    __tablename__ = "confessions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    category = Column(String, nullable=True)
    is_anonymous = Column(Integer, default=1) 