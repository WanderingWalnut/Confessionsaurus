import os
from typing import Optional
from ..models.gemini import ModerationResponse
from dotenv import load_dotenv
import json
from app.services.gemini_client import model

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
        
        Review the confession and return ONLY a valid JSON object.

        ❌ Do NOT include any extra text, explanation, or formatting.
        ❌ Do NOT wrap the response in triple backticks or use markdown.
        ✅ Your entire response should be a single line of raw JSON, like:
        
        Example responses:
        {{"flagged": false, "reason": null}}
        {{"flagged": true, "reason": "Contains hate speech (Guideline 1)"}}
        """
        
        # Get response from Gemini
        response = model.generate_content(prompt)
        print("Raw response text: ", response.text)
        parsed_json = json.loads(response.text)

        result = ModerationResponse(**parsed_json)
        print("Result: ", result)

        print(f"Moderation Successful!")

        return result

    except Exception as e:
        return ModerationResponse(
            flagged=True,  # Be conservative - flag on error
            reason=f"Moderation error: {str(e)}"
        )
# def geneerate_caption():
""" Create this function, creates caption for post based on the content of the post"""

if __name__ == "__main__":
    confession = "I WANNA Kill Myself 😭"
    
    result = moderate_confession(confession)
    print(f"Moderation Result:")
    print(f"Flagged: {result.flagged}")
    print(f"Reason: {result.reason}")
