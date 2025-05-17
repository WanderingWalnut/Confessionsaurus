from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text


class Confessions(Base):
    __tablename__ = "confessions"

    # Confession ID
    id = Column(Integer, primary_key=True)
    # title = Column(String, nullable=False) # Do not need atm
    content = Column(String, nullable=False) # nullable=False means it is required for insertion
    published = Column(Boolean, server_default='FALSE') 
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))



