def get_response(user_message):
    user_message = user_message.lower()

    responses = {
        "/start": "Hola, soy Dark Chat 1.0. ¿En qué puedo ayudarte?",
        "hola": "¡Hola! ¿Cómo estás?",
        "cómo estás": "Estoy bien, gracias por preguntar. ¿Y tú?",
        "adiós": "Hasta luego, que tengas un buen día 😊",
        "gracias": "¡De nada! 😊",
    }

    for key in responses:
        if key in user_message:
            return responses[key]

    return "No entendí tu mensaje. ¿Puedes reformularlo?"
