import os
from google import genai
#from dotenv import load_dotenv

# ✅ Load environment variables
#load_dotenv()

# ✅ Get API key from environment
#api_key = os.getenv("GEMINI_API_KEY")

# ✅ Initialize Gemini client with explicit key
#client = genai.Client(api_key=api_key)
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

def generate_gemini_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        return "⚠️ Unable to generate response at the moment."