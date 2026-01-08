import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY is not set")

