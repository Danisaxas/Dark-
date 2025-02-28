from flask import Flask, render_template, request, jsonify
from responses import get_response  # Importamos las respuestas desde responses.py

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_response = get_response(user_message)  # Llamamos a la función en responses.py
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
