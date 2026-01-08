import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# These are optional during development but required in production
if not os.getenv("RENDER") and not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not set - some features will be unavailable")

if not os.getenv("RENDER") and not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not set - vision features will be unavailable")

