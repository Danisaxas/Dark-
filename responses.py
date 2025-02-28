def get_response(user_message):
    user_message = user_message.lower()

    if user_message == "/start":
        return "Hola, soy Dark Chat 1.0. ¿En qué puedo ayudarte?"
    
    elif "hola" in user_message:
        return "¡Hola! ¿Cómo estás?"
    
    elif "adiós" in user_message or "bye" in user_message:
        return "Hasta luego, que tengas un buen día 😊"
    
    else:
        return "No entendí tu mensaje. ¿Puedes reformularlo?"
