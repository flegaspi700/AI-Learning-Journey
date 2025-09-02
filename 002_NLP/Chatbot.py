import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the generative AI model with the API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Define the model to use
model = genai.GenerativeModel('gemini-1.5-flash')

# Define the conversation (now using Gemini's format)
# The initial system prompt is now part of the model's instructions
chat = model.start_chat(history=[
    {
        "role": "user",
        "parts": ["What is the most famous landmark in Paris?"]
    },
    {
        "role": "model",
        "parts": ["The most famous landmark in Paris is the Eiffel Tower."]
    },
])

# Define a list of questions
questions = [
    "How far away is the Louvre from the Eiffel Tower (in driving miles)?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]

# Loop through each question to generate responses
for question in questions:
    print(f"> User: {question}")
    
    # Send the message to the model
    response = chat.send_message(question)
    
    # Print the response from the model
    print(f"> Gemini: {response.text}")

