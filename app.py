from flask import Flask, request, jsonify, g

app = Flask(__name__)

# Cargar el modelo y el tokenizador entrenados
@app.route('/pregunta', methods=['POST'])
def responder_pregunta():
    data = request.get_json()
    question = data['question']
    respuesta = 'Administración Nacional de Electricidad (ANDE)'

    return jsonify({'respuesta': respuesta})

if __name__ == '__main__':
    app.run(port=5000)
