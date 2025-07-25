import os
import google.generativeai as genai
from google.generativeai import types
from dotenv import load_dotenv

# load env variables
# load_dotenv()  # Commented out for Lambda - env vars set in AWS console

# Configure Gemini Client
# client = genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Commented out for Lambda
client = genai.configure(api_key=os.environ['GEMINI_API_KEY'])  # Lambda-compatible
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")