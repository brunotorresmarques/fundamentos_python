# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja"]

# O 'for' percorre cada elemento diretamente
for fruta in frutas:
    # A variável 'fruta' recebe o valor do item da vez
    print(f"Melhor fruta: {fruta}")



# Lista de carros
carros = ["Fusca", "Civic", "Tesla"]

# range(len(carros)) gera uma sequência de números de 0 até 2
for i in range(len(carros)):
    # Usamos o índice 'i' para acessar o valor correspondente
    print(f"Posição {i}: {carros[i]}")



animais = ["Gato", "Cachorro", "Pássaro"]

# O enumerate devolve uma tupla contendo (índice, valor) a cada iteração
for indice, animal in enumerate(animais):
    print(f"O animal número {indice} é o {animal}")


# Criando um dicionário de produto
produto = {
    "nome": "Notebook",
    "preco": 4500,
    "estoque": 10
}

# Comportamento padrão: Itera pelas CHAVES (Como o for...in)
print("--- Chaves ---")
for chave in produto:
    print(f"Chave: {chave}")

# Iterando pelos VALORES
print("\n--- Valores ---")
for valor in produto.values():
    print(f"Valor: {valor}")

# Iterando por CHAVE e VALOR simultaneamente
print("\n--- Pares Chave:Valor ---")
for chave, valor in produto.items():
    print(f"{chave}: {valor}")