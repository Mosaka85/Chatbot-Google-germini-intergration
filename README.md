## Chatbot-Google-germini-intergration
Flask web application that acts as a chatbot. Intergrated with Google Germini using API calls.

# Imports:
The code imports necessary libraries like Flask for web development, request to handle user requests, jsonify to convert data to JSON format, and render_template to render HTML templates.

# enerativeAI Configuration: The code sets up a connection to the Gemini-Pro model using the provided API key.


Chatbot Response Function: This function takes a user's message as input, sends it to the GenerativeAI model, and returns the generated response.
Flask Routes:

The / route renders the main HTML page for the chat interface.

The /chat route handles user messages and sends them to the chatbot function.

HTML Chat Interface: This is the user interface where users can type their messages and see the chatbot's responses.

JavaScript: The JavaScript code sends user messages to the server and updates the chat history with the chatbot's responses.

In summary, this code creates a web application that allows users to interact with a chatbot powered by Google's GenerativeAI service.
