from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")

print("OpenAI API Key Loaded:", key+ "..." if key else "NOT FOUND")
