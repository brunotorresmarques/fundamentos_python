# 1. *args (Arguments)

def listar_convidados(*nomes):
    # 'nomes' agora é uma tupla contendo todos os argumentos passados
    print(f"Tipo de dado gerado: {type(nomes)}")
    
    for nome in nomes:
        print(f"Inquilino: {nome}")

# Testando com diferentes quantidades de argumentos
listar_convidados("Alice", "Bruno", "Carlos")


# 2. **kwargs (Keyword Arguments)
def salvar_produto(nome, preco, **detalhes):
    # 'detalhes' vira um dicionário com tudo que sobrou
    print(f"Produto: {nome} - R${preco}")
    print(f"Dicionário gerado: {detalhes}")
    
    # Podemos percorrer como um dicionário normal
    for chave, valor in detalhes.items():
        print(f"  {chave}: {valor}")

# Testando e adicionando especificações variadas
salvar_produto("Celular", 2500, marca="Apple", modelo="iPhone 13", cor="Preto")
