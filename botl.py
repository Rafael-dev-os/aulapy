import random
import getpass
from google import genai
from google.genai import types
user_key = input("Please enter your Gemini API Key: ")
def random_number():
    output = random.randint(0, 10)
    return output
def random_shakephere():
    shale = ["Break the ice","Wild-goose chase","Green-eyed monster","Wear your heart upon your sleeve","Too much of a good thing","Neither rhyme nor reason","In a pickle","Laughing stock","Brave new world","Cruel to be kind"]
    return random.choice(shale)
def ask_gemini(prompt: str, api_key: str = user_key, model_name: str = "gemini-2.5-flash") -> str:
    """Sends a text prompt to Gemini using the provided API key."""
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model=model_name,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are named 'le bot', your messages have to be below 2000 characters."
        )
    )
    return response.text
