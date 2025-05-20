# Handles everything related to posting

import os
from dotenv import load_dotenv
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, ClientError

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



if __name__ == "__main__":
    test_instagram_connection()

