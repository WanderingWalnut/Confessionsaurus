from google import genai
import os
from google import genai
import os
from typing import Optional
from ..models.gemini import ModerationResponse

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def moderate_confession(content: str) -> ModerationResponse:
    """
    Moderate a confession using Gemini.
    
    Args:
        content (str): The confession text to moderate
        
    Returns:
        ModerationResponse: Contains moderation decision and details
    """
    try:
        # Create a prompt for moderation
        prompt = f"""
        You are a content moderator for a university confessions page. 
        Review the following confession and determine if it violates any guidelines.
        
        Guidelines:
        - No hate speech or discrimination
        - No explicit sexual content
        - No personal attacks or harassment
        - No doxxing or sharing personal information
        - No illegal content
        - No spam or advertising
        
        Confession: {content}
        
        Respond in this exact format:
        CLEAN: [confidence 0-1] if appropriate
        FLAG: [reason] | [categories] | [confidence 0-1] if violates guidelines
        
        Example responses:
        CLEAN: 0.95
        FLAG: Contains hate speech | hate_speech,harassment | 0.98
        """
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        result = response.text.strip().upper()
        
        # Parse response
        if result.startswith("CLEAN"):
            # Extract confidence if provided
            confidence = float(result.split(":")[1].strip()) if ":" in result else None
            return ModerationResponse(
                is_clean=True,
                confidence=confidence
            )
            
        elif result.startswith("FLAG"):
            # Parse the flagged response
            parts = result[5:].strip().split("|")
            reason = parts[0].strip() if len(parts) > 0 else "Content violates guidelines"
            categories = [c.strip() for c in parts[1].split(",")] if len(parts) > 1 else None
            confidence = float(parts[2].strip()) if len(parts) > 2 else None
            
            return ModerationResponse(
                is_clean=False,
                reason=reason,
                flagged_categories=categories,
                confidence=confidence
            )
            
        else:
            # If we get an unexpected response, be conservative and flag it
            return ModerationResponse(
                is_clean=False,
                reason="Unable to verify content safety",
                confidence=0.5
            )
            
    except Exception as e:
        # If moderation fails, be conservative and flag it
        return ModerationResponse(
            is_clean=False,
            reason=f"Moderation error: {str(e)}",
            confidence=0.5
        )