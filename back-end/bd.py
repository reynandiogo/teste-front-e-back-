import mysql.connector

# Connectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="localhost",
    port = 3306,
    user="backend_user",
    password="senha1234",)

# Criar um cursor para executar comandos SQL
cur = conexao.cursor()

# Executar query para verificar a conexão
cur.execute("SELECT CURDATE();")

row = cur.fetchone()
print("Data atual: {0}".format(row[0]))

# Fechar cursor e conexão
conexao.close()