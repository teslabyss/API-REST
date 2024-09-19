from flask import Flask, request, jsonify # Codigo json a arreglo

# Inicializamos la aplicación Flask
app = Flask(__name__) #

# Definimos una ruta que responderá al método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    # Mensaje de saludo
    # Nos transforma el mensaje a json
    return jsonify({"mensaje": "¡Hola! Bienvenido a la API de saludo."})

# Ejecutamos la aplicación sin modulos externos
if __name__ == '__main__':
    app.run(debug=True) #Ejecuta un servidor en modo de depuración
