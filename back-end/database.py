import sqlite3

def criar_conexao():
    conn = sqlite3.connect('produtos.db')
    return conn

def criar_tabela():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome VARCHAR(100) NOT NULL,
        preco FLOAT,
        estoque INTEGER
    );''')

    conn.commit()
    conn.close()

def criar_produto(nome=str, preco=float, estoque=int):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?,?,?)', (nome,preco,estoque))

    conn.commit()
    conn.close()

def listar_produtos():
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute('SELECT * FROM produtos')

    resultado = cur.fetchall()
    conn.close()

    return resultado

def atualizar_produto(id_atualizar, novo):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute(f'UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?', (novo['nome'], novo['preco'], novo['estoque'], id_atualizar))

    conn.commit()
    conn.close()

def deletar_produto(id_deletar):
    conn = criar_conexao()
    cur = conn.cursor()

    cur.execute('DELETE FROM produtos WHERE id = ?', (id_deletar,))

    conn.commit()
    conn.close()