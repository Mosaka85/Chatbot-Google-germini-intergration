# Chatbot-Google-germini-intergration
A Flask web application that serves as a chatbot, integrated with Google Gemini AI using API calls to generate intelligent responses.

# Project Overview
This project demonstrates the integration of Google's Gemini model into a Flask-based chatbot. It showcases how to leverage a powerful AI system to interact with users, respond to queries, and engage in meaningful conversation via a web-based interface.

# Key Features
Flask Framework: This project uses Flask, a lightweight and flexible web framework, to handle HTTP requests and serve dynamic content.
Generative AI Integration: Google's Gemini-Pro model is integrated using API calls, allowing the chatbot to generate content based on user prompts.
Dynamic Chat Interface: A clean and simple web interface allows users to chat with the AI bot in real-time.
Error Handling: The system includes enhanced error handling for API calls and user input validation.
File Structure
app.py: The main application file that contains the Flask routes and logic to connect with the Google Gemini model.
templates/MosakaChat.html: The HTML template for the chat interface, where users can interact with the chatbot.
static: Directory containing static files such as JavaScript, CSS, and images used in the web application.
Code Walkthrough

# Imports
The code imports necessary libraries such as:

*Flask* : For building the web application.
*request* : To handle incoming POST requests from users.
*jsonify* : To convert Python dictionaries into JSON format.
render_template: To render the HTML chat interface.
google.generativeai: For accessing the Google Gemini model via API calls.
GenerativeAI Configuration
The application sets up a connection to the Gemini-Pro model using an API key, which is securely retrieved from environment variables. This API key allows the app to authenticate requests to the Google GenerativeAI service.

Chatbot Response Function
This function, chatbot_response(), processes user input by sending the prompt to the Gemini model and returning a response. It also replaces certain keywords like "Gemini" with custom terms such as "MOSAKA Intelligence" and "Google" with "Tshepiso Ndaba" to personalize responses.

Flask Routes
/ (index): Renders the main HTML page (MosakaChat.html), where users can interact with the chatbot.
/chat: Handles incoming chat requests by receiving user input in JSON format, passing it to the chatbot_response() function, and returning the AI-generated response.
HTML Chat Interface
The main interface is designed in MosakaChat.html, providing a simple chatbox for users to input their messages and receive responses from the chatbot.

JavaScript Integration
JavaScript handles the asynchronous communication between the front-end (HTML chat interface) and the back-end Flask server. User messages are sent to the /chat route, and responses are displayed dynamically on the page.

Running the Application
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the Gemini API key:

bash
Copy code
export GEMINI_API_KEY='your-api-key-here'
Run the Flask application:

bash
Copy code
python app.py
Open your browser and navigate to:

arduino
Copy code
http://localhost:5000
Future Improvements
Enhanced UI/UX: Improve the chat interface to make it more user-friendly and visually appealing.
Logging and Analytics: Implement logging for tracking chatbot performance and capturing user insights.
Natural Language Processing: Further refine the AI model's responses by incorporating additional NLP techniques.
