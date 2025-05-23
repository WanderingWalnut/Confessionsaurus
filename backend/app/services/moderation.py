from google import genai
import os
from google import genai
import os
from typing import Optional
from ..models.gemini import ModerationResponse
import json

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
        1. No hate speech or discrimination
        2. No explicit sexual content
        3. No personal attacks or harassment
        4. No doxxing or sharing personal information
        5. No illegal content
        6. No spam or advertising
        
        Confession: {content}
        
        Review the confession and return a JSON object with the following structure:
        {{
            "flagged": true/false,
            "reason": "short reason for flagging or null"
        }}
        
        Example responses:
        {{"flagged": false, "reason": null}}
        {{"flagged": true, "reason": "Contains hate speech (Guideline 1)"}}
        """
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        result = json.loads(response.text)

        print(f"Moderation Successful! Here is the response: {result["flagged"]} and {result["reason"]}")

    except Exception as e:
        return ModerationResponse(
            flagged=True,  # Be conservative - flag on error
            reason=f"Moderation error: {str(e)}"
        )
