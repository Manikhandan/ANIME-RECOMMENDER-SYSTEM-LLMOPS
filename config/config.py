import os
from dotenv import load_dotenv

load_dotenv()

## ingatha .env file la irnthu env eh eduthu vanthu inga store pani vakrom
GROQ_API_KEY= os.getenv("groq_api_key")
MODEL_NAME = "llama-3.1-8b-instant"
