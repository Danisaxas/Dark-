import json
from flask import Flask, render_template, request, jsonify
from responses import get_response

app = Flask(__name__)

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
    bot_response = get_response(user_message)

    chat_entry = {"user": user_message, "bot": bot_response}
    
    history = load_chat_history()
    history.append(chat_entry)
    save_chat_history(history)

    return jsonify({"response": bot_response, "history": history})

if __name__ == "__main__":
    app.run(debug=True)
