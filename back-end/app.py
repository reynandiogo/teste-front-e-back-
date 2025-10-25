from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route("/login", methods=["POST"])
def login():
    # 1️⃣ Receber os dados JSON enviados pelo front
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    # 2️⃣ Fazer alguma verificação (exemplo simples)
    if usuario == 'admin' and senha == '1234':
        # 3️⃣ Retornar um JSON dizendo que deu certo
        return jsonify({'sucesso': True})
    else:
        # 4️⃣ Retornar um JSON dizendo que deu errado
        return jsonify({'sucesso': False})

if __name__ == '__main__':
    app.run(debug=True)
