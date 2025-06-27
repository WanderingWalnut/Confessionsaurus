# Placeholder for SQLAlchemy confession model
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, Enum as PgEnum
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

Base = declarative_base()

class ConfessionStatus(str, Enum):
    new = "NEW"
    pending = "PENDING"
    ready = "READY"
    posted = "POSTED"

class Confession(Base):
    __tablename__ = "confessions"
    
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    status = Column(PgEnum(ConfessionStatus), nullable=False, default=ConfessionStatus.new)
    reason = Column(String, nullable=True)