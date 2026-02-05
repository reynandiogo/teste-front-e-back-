from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

# Rota para listar todos os produtos
@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = database.listar_produtos()
    lista_produtos = []

    for produto in produtos:
        produto_dict = {
            'id': produto[0],
            'nome': produto[1],
            'preco': produto[2],
            'estoque': produto[3]
        }
        lista_produtos.append(produto_dict)

    return make_response(jsonify(lista_produtos), 200)

# Rota para criar um novo produto
@app.route('/produtos', methods=['POST'])
def post_produto():
    dados = request.get_json()
    nome = dados.get('nome')
    preco = dados.get('preco')
    estoque = dados.get('estoque')
    database.criar_produto(nome, preco, estoque)

    return make_response(jsonify({'mensagem': 'Produto criado com sucesso!'}), 201)

@app.route('/produtos/<int:id>', methods=['PUT'])
def put_produto(id):
    dados = request.get_json()
    database.atualizar_produto(id, dados)

    return make_response(jsonify({'mensagem': 'Produto atualizado com sucesso!'}), 200)

@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    database.deletar_produto(id)

    return make_response(jsonify({'mensagem': 'Produto deletado com sucesso!'}), 200)

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