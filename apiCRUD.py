from flask import Flask, request, jsonify
import requests

# URL base de la API Mock
BASE_URL = "https://66eb019a55ad32cda47b4cc5.mockapi.io/IoTCarStatus"

# Inicializamos la aplicación Flask
app = Flask(__name__)

# Ruta para obtener todos los registros (GET)
@app.route('/cars', methods=['GET'])
def get_cars():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Error al obtener los datos"}), response.status_code

# Ruta para obtener un coche por ID (GET)
@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    response = requests.get(f"{BASE_URL}/{car_id}")
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"Error al obtener el coche con ID {car_id}"}), response.status_code

# Ruta para crear un nuevo coche (POST)
@app.route('/cars', methods=['POST'])
def create_car():
    new_car_data = request.json  # Obtener los datos del nuevo coche del cuerpo de la petición
    response = requests.post(BASE_URL, json=new_car_data)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({"error": "Error al crear el coche"}), response.status_code

# Ruta para actualizar un coche existente (PUT)
@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    updated_car_data = request.json  # Obtener los datos actualizados del cuerpo de la petición
    response = requests.put(f"{BASE_URL}/{car_id}", json=updated_car_data)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": f"Error al actualizar el coche con ID {car_id}"}), response.status_code

# Ruta para eliminar un coche (DELETE)
@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    response = requests.delete(f"{BASE_URL}/{car_id}")
    if response.status_code == 200:
        return jsonify({"mensaje": f"Coche con ID {car_id} eliminado"})
    else:
        return jsonify({"error": f"Error al eliminar el coche con ID {car_id}"}), response.status_code

# Ejecutamos la aplicación
if __name__ == '__main__':
    app.run(debug=True)
