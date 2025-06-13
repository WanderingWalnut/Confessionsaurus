from pydantic import BaseModel
from typing import Optional

class ModerationResponse(BaseModel):
    """
    Simple model for Gemini's moderation response.
    """
    flagged: bool  # True if content violates guidelines, False if clean
    reason: Optional[str] = None  # Reason for flagging, or None if clean