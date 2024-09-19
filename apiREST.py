from flask import Flask, request, jsonify

# Inicializamos la aplicación Flask
app = Flask(__name__)


# Ruta que acepta múltiples métodos HTTP
@app.route('/saludo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo():
    # Manejo del método GET
    if request.method == 'GET':
        return jsonify({"mensaje": "¡Hola! Bienvenido a la API de saludo (GET)."})

    # Manejo del método POST
    elif request.method == 'POST':
        return jsonify({"mensaje": "¡Saludo recibido mediante POST!"})

    # Manejo del método PUT
    elif request.method == 'PUT':
        return jsonify({"mensaje": "¡Saludo actualizado mediante PUT!"})

    # Manejo del método DELETE
    elif request.method == 'DELETE':
        return jsonify({"mensaje": "¡Saludo eliminado mediante DELETE!"})


# Ejecutamos la aplicación
if __name__ == '__main__':
    app.run(debug=True)
