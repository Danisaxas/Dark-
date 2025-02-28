import json
import openai
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_pymongo import PyMongo
from auth import auth
from responses import get_response
from config import MONGO_URI, OPENAI_API_KEY

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI
app.config["SECRET_KEY"] = "clave_secreta_super_segura"

mongo = PyMongo(app)
openai.api_key = OPENAI_API_KEY
app.register_blueprint(auth, url_prefix="/auth")

CHAT_HISTORY_FILE = "chat_history.json"

@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("chat"))
    return redirect(url_for("auth.login"))

@app.route("/chat")
def chat():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    
    chat_history = load_chat_history()
    return render_template("index.html", chat_history=chat_history)

@app.route("/chat", methods=["POST"])
def chat_post():
    if "user_id" not in session:
        return jsonify({"response": "Debes iniciar sesión para chatear."})

    user_message = request.json.get("message", "").strip()

    if user_message.startswith("/"):
        bot_response = get_response(user_message)
    else:
        bot_response = get_ai_response(user_message)

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

def load_chat_history():
    try:
        with open(CHAT_HISTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_chat_history(history):
    with open(CHAT_HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)

if __name__ == "__main__":
    app.run(debug=True)
