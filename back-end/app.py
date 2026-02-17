from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    user = dados.get('usuario')
    senha = dados.get('senha')

    if user == 'admin' and senha == 'admin':
        return make_response(jsonify({'sucesso': True}), 200)
    else:
        return make_response(jsonify({'sucesso': False}), 401)

if __name__ == '__main__':
    app.run(debug=True)