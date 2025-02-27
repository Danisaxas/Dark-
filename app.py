from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Obtiene el puerto de la variable de entorno, si no está disponible usa el puerto 5000
    port = int(os.environ.get("PORT", 5000))  
    # Ejecuta la aplicación en el puerto y host correcto para Heroku
    app.run(debug=True, host='0.0.0.0', port=port)