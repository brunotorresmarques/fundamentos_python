import sqlite3

# 1 - Criando a conexão com o banco de dados SQLite
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# 2 - Inserindo dados
cursor.execute(
    """
        INSERT INTO filmes(nome, ano, nota)
        VALUES ('Filme 2', 2020, 8.5)
    """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")