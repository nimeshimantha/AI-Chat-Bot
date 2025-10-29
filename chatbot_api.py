from google import genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize client correctly
client = genai.Client(api_key=API_KEY)

def create_chat_session(model_name="gemini-2.5-flash"):
    """Create a new chat session with the AI model."""
    return client.chats.create(model=model_name)

def send_message(chat_session, message):
    """Send a message to the AI and return the response as a string."""
    response_stream = chat_session.send_message_stream(message)
    reply = ""
    for chunk in response_stream:
        reply += chunk.text
    return reply
