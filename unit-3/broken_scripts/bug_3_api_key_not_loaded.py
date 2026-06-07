import os

# BUG: Attempting to retrieve OPENAI_API_KEY without calling load_dotenv() first
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("CRASHED: API key is None!")
else:
    print("API Key Loaded successfully:", api_key[:4] + "***")
