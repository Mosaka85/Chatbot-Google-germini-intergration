from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai
app = Flask(__name__)
api_key = "AIzaSyCBZyG0fVJfmnjOO0pEyrfUbkVDiCvt7gU"
if not api_key:
    raise ValueError("Missing  environment variable. Set it before running the app.")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
def chatbot_response(prompt):

    try:
        response = model.generate_content(prompt)
        response_text = response.text.replace("Gemini", "MOSAKA Intelligence")
        response_text = response_text.replace("Google", "Tshepiso Ndaba")
        return response_text
    except Exception as e:
        print(f"Error generating response: {e}")
        return "An error occurred. Please try again later."
@app.route("/")
def index():
    if not os.path.exists("MosakaChat.html"):
        raise FileNotFoundError("Chat interface template (MosakaChat.html) not found. Create it.")
    return render_template("MosakaChat.html")
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("prompt")
    print(f"Received input: {user_input}")
    if not user_input:
        return jsonify({"error": "Please provide a question or message to start the chat."}), 400
    response = chatbot_response(user_input)
    print(f"Generated bot response: {response}")
    return jsonify({"response": response})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
