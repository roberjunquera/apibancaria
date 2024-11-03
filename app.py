from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulando una base de datos en memoria
cuentas = []

@app.route('/cuentas', methods=['GET'])
def obtener_cuentas():
    return jsonify(cuentas)

@app.route('/cuentas', methods=['POST'])
def crear_cuenta():
    nueva_cuenta = request.json
    cuentas.append(nueva_cuenta)
    return jsonify(nueva_cuenta), 201

@app.route('/cuentas/<int:cuenta_id>', methods=['GET'])
def obtener_cuenta(cuenta_id):
    cuenta = next((c for c in cuentas if c.get('id') == cuenta_id), None)
    return jsonify(cuenta) if cuenta else ('', 404)

@app.route('/cuentas/<int:cuenta_id>', methods=['PUT'])
def actualizar_cuenta(cuenta_id):
    cuenta = next((c for c in cuentas if c.get('id') == cuenta_id), None)
    if cuenta:
        datos_actualizados = request.json
        cuenta.update(datos_actualizados)
        return jsonify(cuenta)
    return ('', 404)

@app.route('/cuentas/<int:cuenta_id>', methods=['DELETE'])
def eliminar_cuenta(cuenta_id):
    global cuentas
    cuentas = [c for c in cuentas if c.get('id') != cuenta_id]
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
