import os
import google.generativeai as genai
from google.generativeai import types
from dotenv import load_dotenv

# load env variables
load_dotenv()

# Configure Gemini Client
client = genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")