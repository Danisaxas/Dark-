import random

def get_response(user_message):
    user_message = user_message.lower()

    commands = {
        "/start": "¡Hola! Soy Dark Chat 1.0 🤖. Pregúntame lo que quieras.",
        "/help": "Comandos disponibles:\n/start - Iniciar chat\n/help - Ver comandos\n/about - Info del bot\n/random - Número aleatorio",
        "/about": "Dark Chat 1.0 es un chatbot con IA integrado usando OpenAI GPT.",
        "/random": f"Tu número aleatorio es: {random.randint(1, 100)}",
        "/image": '<img src="/static/images/example.jpg" width="200px">'
    }

    return commands.get(user_message, "No reconozco ese comando. Usa /help para ver los disponibles.")
