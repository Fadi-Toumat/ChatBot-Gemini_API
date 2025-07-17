# gemini_service.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Configure the Generative AI client with API key from environment variables
# Ensure GOOGLE_API_KEY is set in your .env file or as a system environment variable
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")

genai.configure(api_key=google_api_key)

def get_gemini_response(user_message: str) -> str:
    """
    Sends a user message to a Google Gemini Pro model and returns the bot's response.

    Args:
        user_message (str): The message from the user.

    Returns:
        str: The AI's response text, or an error message if an issue occurs.
    """
    try:
        # Initialize the Generative Model
        model = genai.GenerativeModel('gemini-pro')
        
        # Start a new chat session
        # For a simple turn-based chatbot, you can just use generate_content
        # For conversational memory, you would use model.start_chat() and pass history
        
        response = model.generate_content(user_message)
        
        # Access the text from the response
        # Ensure that the response contains text (Gemini can return other types of content)
        if response.parts:
            return response.text
        else:
            print(f"Gemini response had no text content: {response}")
            return "Sorry, Gemini returned no text content for your query."

    except Exception as e:
        # Log the actual error for debugging purposes (this will appear in your console/logs)
        print(f"Error connecting to Google Gemini: {e}")
        # Return a user-friendly error message
        return "Sorry, an error occurred while processing your request with Gemini. Please try again later."