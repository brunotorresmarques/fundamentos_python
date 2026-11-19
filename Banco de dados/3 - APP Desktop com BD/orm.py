from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///banco.db', echo=True)
Base = declarative_base()


class Filme(Base):
    __tablename__ = 'filmes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

Base.metadata.create_all(engine)

# Inserir dados
def insere_dados(nome, ano, nota):
    Session = sessionmaker(bind=engine)
    session = Session()
    novo_filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(novo_filme)
    session.commit()
    session.close()

# insere_dados("Exemplo de Filme", 2023, 8.5)
# insere_dados("Outro Filme", 2022, 7.2)

# Atualizar dados
def atualizar_dados(filme_id, nome=None, ano=None, nota=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=filme_id).first()
    if filme:
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        session.commit()
    session.close()

# atualizar_dados(1, nome="Filme Atualizado", nota=9.0)

# Excluir filme
def excluir_filme(filme_id):
    Session = sessionmaker(bind=engine)
    session = Session()
    filme = session.query(Filme).filter_by(id=filme_id).first()
    if filme:
        session.delete(filme)
        session.commit()
    session.close()

# excluir_filme(2)

# Consultar dados
def obter_dados():
    Session = sessionmaker(bind=engine)
    session = Session()
    filmes = session.query(Filme).all()
    session.close()
    return [(filme.id, filme.nome, filme.ano, filme.nota) for filme in filmes]

# obter_dados()