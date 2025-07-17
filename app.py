# app.py (Gradio interface)

import os
import gradio as gr
# Import the Gemini service function directly
from gemini_service import get_gemini_response

def chat_interface(message, history):
    """
    Gradio interface function to handle chat messages.
    It directly calls the Gemini service function to get the response.
    """
    try:
        # Directly call the get_gemini_response function
        bot_response = get_gemini_response(message)
        
        # Gradio's ChatInterface automatically handles history,
        # so we just return the bot_response.
        return bot_response
    except Exception as e:
        print(f"An unexpected error occurred in Gradio interface: {e}")
        return "Sorry, an unexpected error occurred while processing your request with Gemini."

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chat_interface,
    title="Gemini Pro Chatbot",
    description="Ask me anything!",
    examples=[
        "What is the capital of France?",
        "Tell me a short story about a brave knight.",
        "Explain AI in simple terms."
    ],
    chatbot=gr.Chatbot(height=400) # Sets the height of the chat display
)

# Launch the Gradio app
if __name__ == "__main__":
    # Get the port from the environment variable provided by Hugging Face (default Gradio port is 7860)
    port = int(os.environ.get("PORT", 7860))
    # server_name="0.0.0.0" is important for Hugging Face to make the app accessible.
    demo.launch(server_name="0.0.0.0", server_port=port)