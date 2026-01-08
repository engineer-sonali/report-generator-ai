import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OPENAI_API_KEY is required in production
if not os.getenv("RENDER") and not OPENAI_API_KEY:
    print("Warning: OPENAI_API_KEY not set - report generation will not work")

