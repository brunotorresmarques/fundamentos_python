import sqlite3

# Criando a conexão com o banco de dados SQLite
conexao = sqlite3.connect('titulo.db')

# 2 - Criando o cursor para executar comandos SQL
cursor = conexao.cursor()

# 3 - Criando a tabela
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
    )
    '''
)


# 4 - Fechar a conexão com o banco de dados
conexao.close()

print("Tabela 'filmes' criada com sucesso!")