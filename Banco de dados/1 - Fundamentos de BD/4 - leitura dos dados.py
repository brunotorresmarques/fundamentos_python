import sqlite3

# 1 - Conexão
conexao = sqlite3.connect("titulo.db")
cursor = conexao.cursor()


# 2 - Recebendo dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())