# Handles everything related to posting

import os
from typing import List
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.types import Location
from instagrapi.exceptions import LoginRequired, ClientError
from pathlib import Path
from typing import Optional
import json
from datetime import datetime, timedelta
from app.services.gemini_client import model
from app.db.session import SessionLocal
from app.db.crud_confession import create_confession
from ..models.gemini import CaptionResponse

class InstagramSessionManager:

    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.client = Client()
        self.session_file = Path(__file__).parent.parent/ "data" / "instagram_session.json" # Created under app folder
        self.session_file.parent.mkdir(exist_ok=True) # Makes sure data folder exists and prevents error if it alr exists
        self.last_login = None # Tracks the last time you logged in (validation for session expiration) i.e current time - last logged in
        self.session_duration = timedelta(hours = 24) # Session expires after 24 hours
        print("Session file will be saved at:", self.session_file.resolve())

    
    # _ stands for private functions/methods, do not call outside of class
    def _save_session(self):
        """ save session to file"""
        # Grab all session data from instagrapi
        session = self.client.get_settings()
        print("Our session data: ", session)

        self.client.dump_settings(self.session_file)
        
        # Open or create the file at self.session_file --> data/insatgram_session.json
        # with open(self.session_file, 'w') as f:
        #     json.dump({
        #         'session': session,
        #         'last_login': datetime.now().isoformat()
        #     }, f, default= lambda x: str(x)) # Lambda function basically makes sure everything is a JSON string (serialized)

    
    def _load_session(self):
        """Load session from file if it exists and is valid """

        if not self.session_file.exists():
            print("Session does not exist")
            return False

        try:
            # Load session from past login
            self.client.load_settings(self.session_file)

            # Verify the session is still valid
            try:
                self.client.get_timeline_feed()
                print("Session Logged In Successfully! (Loaded)")
                return True
            except LoginRequired:
                print("Session expired or invalid ")
                return False
        
        except Exception as e:
            print(f"Error loading session: {str(e)}")
            return False
        
        # except Exception:
        #     print("Session file was corrupt or unreadable. Deleting it.")
        #     self.session_file.unlink(missing_ok=True)
        #     return False
        
        except Exception as e:
            print(f'An error has occurred {str(e)}')
            return False
        

    def ensure_login(self):
        """ Load session from file if it exists"""

        if self._load_session():
            try:
                self.client.get_timeline_feed()
                return True
        
            except LoginRequired:
                print('Login is required, will try logging in now')
                pass
    
        """ Login if session from file does not exist/not valid """
        try:
            # Load credentials
            # username = os.getenv("INSTAGRAM_USERNAME")  # Commented out for Lambda
            # password = os.getenv("INSTAGRAM_PASSWORD")  # Commented out for Lambda
            username = os.environ['INSTAGRAM_USERNAME']  # Lambda-compatible
            password = os.environ['INSTAGRAM_PASSWORD']  # Lambda-compatible

            # Login
            try:
                self.client.login(username, password)
                print("Attempting Login...")
            except Exception as e:
                raise Exception(f'Instagram login failed: {e}')

            # Save session data
            self._save_session()
            self.last_login = datetime.now()
            return True
    
        except Exception as e:
            print(f'Failed to login to Instagram {str(e)}')
            return False
    
    def create_caption(self, confessions: list[str]):
        """ Creates a caption thru gemini based on content of confessions """

        formatted_confession = []

        # Format confessions to give Gemini more context on what each confession is about and which slide
        for i in range(len(confessions)):
            formatted_confession.append(f"Slide {i+1}: {confessions[i]}")
        
        confession_content = '\n'.join(formatted_confession)
        
        
        prompt = f"""
        You are an Instagram social media manager for a university confessions page.

        Your goal is to generate a single, fun, engaging, and highly relatable caption for a carousel post based on the set of confessions below.

        Guidelines:
        - Write in a casual, energetic, and meme-like tone.
        - Use phrases like "HELL NOOOO", "what y'all think?", "this one is wild fr 😭", "give advice in the comments‼️" to make the caption feel like it's talking to friends.
        - Make the audience *want* to engage — ask for their thoughts, advice, or reactions.
        - You can tease or reference the confessions, but you do NOT have to mention every slide.
        - Keep it short and punchy, avoid long paragraphs.
        - Emojis are encouraged but don't overdo them (1-2 per line max).
        - End with a direct engagement hook — e.g., "drop your advice 👇" or "who's guilty of this? 😭"

        **IMPORTANT:**
        - Output ONLY one caption as a single line of text.
        - Do NOT include any explanations, options, formatting, or extra text.
        - Do NOT use markdown, bullet points, or headings.
        - Do NOT say anything like "Here is your caption:" or "Option 1:".
        - Just output the caption itself, nothing else.

        **Sample Outputs:**
        - "Y'all ever seen a wilder batch? Slide 2 had me crying 😭 drop your thoughts 👇"
        - "Confessions got me rethinking my life choices... what y'all think??"
        - "This week's confessions are next level 💀 advice for these folks??"
        - "Some of y'all need therapy, not Instagram 😭 who's guilty of this? 👇"
        - "Slide 1 is wild, but Slide 3?? Nah, that's criminal behavior 💀"

        Confessions:
        {confession_content}
        """
        try:
            response = model.generate_content(prompt)
            caption_text = response.text.strip() # Process str response
            print(f"Raw response text for caption: {caption_text}")

            return caption_text
        
        except Exception as e:
            print(f"Failed to create a caption: {e}")
            return None

    def post_photo(self, image_path: str, caption: str):
        """ Post a photo to instagram """
        # Make sure we are logged in
        if not self.ensure_login():
            raise Exception(f'Failed to maintain instagram session {str(Exception)}')
    
        # If image does not exist or invalid path
        # if not image_path.exists():
        #     raise FileNotFoundError(f"Image file not does not exist {str(image_path)}")

        # If we are logged in, upload post
        return self.client.photo_upload(
            str(image_path), # Has to be str for instagrapi
            caption,
            location=Location(name="Canada, Calgary", lat=51.05, lng=114.07)
            )
    
    def post_carousel(self, paths: List[str], caption: Optional[str] = None):
        """ Post carousel/album to instagram """

        # Ensure we are logged in
        if not self.ensure_login():
            raise Exception(f'Failed to maintain instagram session {str(Exception)}')
        
        # If logged in, post the album/carousel
        print("Successfully posted carousel/album!")
        return self.client.album_upload(paths, caption)





