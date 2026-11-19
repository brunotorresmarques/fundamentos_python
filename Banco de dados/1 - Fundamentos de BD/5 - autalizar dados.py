import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# Atualizando dados por ID
id = 2

cursor.execute(
    """
        UPDATE filmes 
        SET nome = ?
        WHERE id = ?
    """,
    ("Filme Atualizado", id)
)

conexao.commit()

print("Dados Atualizados!")