# Handles everything related to posting

import os
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.types import Location
from instagrapi.exceptions import LoginRequired, ClientError
from pathlib import Path
import json
from datetime import datetime, timedelta

class InstagramSessionManager:
    def __init__(self):
        self.client = Client()
        self.session_file = Path(__file__).parent.parent / "data" / "instagram_session.json" # Created under app folder
        self.session_file.parent.mkdir(exist_ok=True) # Makes sure data folder exists and prevents error if it alr exists
        self.last_login = None # Tracks the last time you logged in (validation for session expiration) i.e current time - last logged in
        self.session_duration = timedelta(hours = 24) # Session expires after 24 hours
    
    # _ stands for private functions/methods, do not call outside of class
    def _save_session(self):
        """ save session to file"""
        # Grab all session data from instagrapi
        session = self.client.get_settings()
        
        # Open or create the file at self.session_file --> data/insatgram_session.json
        with open(self.session_file, 'w') as f:
            json.dump({
                'session': session,
                'last_login': datetime.now().isoformat()
            }, f)
    
    def _load_session(self):
        """Load session from file if it exists and is valid """

        if not self.session_file.exists():
            print("Session does not exist")
            return False

        try:
            with open(self.session_file, 'r') as f:
                data = json.load(f)
                last_login = datetime.fromisoformat(data['last_login'])

                # If session has gone for more than 24hrs return false --> new session needed 
                if datetime.now() - last_login > self.session_duration:
                    return False
                
                # Load the session details into client, basically login
                self.client.load_settings(data['session'])
                # Update last login
                self.last_login = last_login

                return True
        
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
        username = os.getenv("INSTAGRAM_USERNAME")
        password = os.getenv("INSTAGRAM_PASSWORD")

        # Login
        self.client.login(username, password)

        # Save session data
        self.session_file = self._save_session()
        self.last_login = datetime.now()
        return True
    
    except Exception as e:
        print(f'Failed to login to Instagram {str(e)}')
        return False

def post_photo(self, image_path: Path, caption: str):
    """ Post a photo to instagram """
    # Make sure we are logged in
    if not self.ensure.login():
        raise Exception(f'Failed to maintain instagram session {str(Exception)}')
    
    # If image does not exist or invalid path
    if not image_path.exists():
        raise FileNotFoundError(f"Image file not does not exist {str(image_path)}")

    # If we are logged in, upload post
    return self.client.photo_upload(
        str(image_path), # Has to be str for instagrapi
        caption,
        location=Location(name="Canada, Calgary", lat=51.05, lng=114.07)
        )




    

# Load environment variables
load_dotenv()

def test_instagram_connection():
    try:
        # Initialize client
        cl = Client()
        
        # Get credentials from environment variables
        username = os.getenv('INSTAGRAM_USERNAME')
        password = os.getenv('INSTAGRAM_PASSWORD')
        
        if not username or not password:
            raise ValueError("Instagram credentials not found in environment variables")
        
        # Attempt login
        cl.login(username, password)
        
        # Get account info
        account_info = cl.account_info().dict()
        print("Successfully connected to Instagram!")
        print(f"Logged in as: {account_info.get('username')}")
        print(f"Account ID: {account_info.get('pk')}")
        return account_info
        
    except LoginRequired as e:
        print(f"Login failed: {str(e)}")
        return None
    except ClientError as e:
        print(f"Instagram client error: {str(e)}")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

def post_instagram(path: str, caption: str):
    try:
        cl = Client()

        # Get credentials from environment variables
        username = os.getenv('INSTAGRAM_USERNAME')
        password = os.getenv('INSTAGRAM_PASSWORD')
        
        cl.login(username, password)

        media = cl.photo_upload(Path, caption, location = Location(name="Canada, Calgary", lat=51.05, lng=114.07))
    
    except LoginRequired as e:
        print(f'User not logged in: {str(e)}')
        return None
    except ClientError as e:
        print(f'Instagram client error: {str(e)}')
        return None
    except Exception as e:
        print(f'Unexpected error occured {str(e)}')
        return None




if __name__ == "__main__":
    test_instagram_connection()

