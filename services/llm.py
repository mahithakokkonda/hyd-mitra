import os
from dotenv import load_dotenv
from google.genai import Client
from prompt import SYSTEM_PROMPT
from services.memory import remember, get_context   # ← added

load_dotenv()
client = Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_llm_response(user_text):

    context = get_context()   # ← added

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents= SYSTEM_PROMPT +
                  "\n\nఇప్పటివరకు జరిగిన సంభాషణ:\n" + context +
                  "\nవాడుకరి ప్రశ్న:\n" + user_text
    )

    remember(user_text, response.text)   # ← added
    return response.text
