import json
import openai
from flask import Flask, render_template, request, jsonify
from config import OPENAI_API_KEY
from responses import get_response

app = Flask(__name__)
openai.api_key = OPENAI_API_KEY

CHAT_HISTORY_FILE = "chat_history.json"

def load_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_chat_history(history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

@app.route("/")
def index():
    chat_history = load_chat_history()
    return render_template("index.html", chat_history=chat_history)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    
    if user_message.startswith("/"):
        bot_response = get_response(user_message)  # Manejar comandos
    else:
        bot_response = get_ai_response(user_message)  # Usar IA de OpenAI
    
    chat_entry = {"user": user_message, "bot": bot_response}
    
    history = load_chat_history()
    history.append(chat_entry)
    save_chat_history(history)

    return jsonify({"response": bot_response, "history": history})

def get_ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente útil."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    app.run(debug=True)
