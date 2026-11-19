import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# Exclusão de dados

id = 2

cursor.execute(
    """
        DELETE FROM filmes WHERE id = ?
    """,
    (id, )
)

conexao.commit()
    
print("Dados excluidos!!")