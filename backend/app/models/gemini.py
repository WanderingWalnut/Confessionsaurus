from pydantic import BaseModel
from typing import Optional

class ModerationResponse(BaseModel):
    """
    Model for Gemini's moderation response.
    This represents what we get back from the Gemini API when moderating a confession.
    """
    is_clean: bool  # Whether the content passed moderation
    reason: Optional[str] = None  # If not clean, why it was flagged
    flagged_categories: Optional[list[str]] = None  # Categories of violations (e.g., ["hate_speech", "harassment"])
    confidence: Optional[float] = None  # How confident Gemini is in its decision (0-1)
    
    class Config:
        from_attributes = True  # Allows conversion from ORM model if needed