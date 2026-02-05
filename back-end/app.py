from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="backend_user",
        password="senha1234",
        database="projeto_teste"
    )
    return conexao