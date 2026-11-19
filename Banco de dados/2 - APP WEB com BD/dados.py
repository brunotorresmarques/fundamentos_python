import sqlite3


# 1- Conexão com Banco de Dados
def conectar_bd():
    conexao = sqlite3.connect('filmes.db')
    return conexao

# 2 - Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)",
        (nome, ano, nota)
    )
    conexao.commit()
    cursor.close()
    conexao.close()


# 3 - Consultar dados
def obter_dados():
    conexao = conectar_bd()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM filmes")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados
