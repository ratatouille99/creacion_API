from flask import Flask, jsonify, request

app = Flask(__name__)

pepamones = [
    {"id": 1, "name": "Pepa", "type": "Puerca"},
    {"id": 2, "name": "George", "type": "Niño dinosaurio"},
    {"id": 3, "name": "Papa cerdo", "type": "Dios"}
]

# Endpoint para obtener todos los Pepamones
@app.route('/pepamones', methods=['GET'])
def get_pepamones():
    return jsonify(pepamones)

# Endpoint para obtener un Pepamón por su nombre
@app.route('/pepamones/nombre/<string:nombre>', methods=['GET'])
def get_pepamon_by_name(nombre):
    for pepamon in pepamones:
        if pepamon['name'].lower() == nombre.lower():
            return jsonify(pepamon)
    return jsonify({'message': 'Pepamón not found'}), 404

# Endpoint para agregar un nuevo Pepamón
@app.route('/pepamones', methods=['POST'])
def add_pepamon():
    new_pepamon = request.get_json()
    if not new_pepamon or 'name' not in new_pepamon or 'type' not in new_pepamon:
        return jsonify({'message': 'Invalid data. Make sure to include name and type'}), 400
    
    # Simulación del ID (en un caso real se podría manejar con una base de datos)
    new_pepamon['id'] = len(pepamones) + 1
    pepamones.append(new_pepamon)
    return jsonify(new_pepamon), 201

if __name__ == '__main__':
    app.run(debug=True)
