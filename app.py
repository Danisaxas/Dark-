from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    if user_message.lower() == "/start":
        bot_response = "Hola, soy Dark Chat 1.0"
    else:
        bot_response = "No entiendo ese comando."
    return jsonify({"response": bot_response})

if __name__ == '__main__':
    app.run(debug=True)