# Criando uma função lambda para somar dois números
soma = lambda x, y: x + y

print(soma(5, 3))  # Saída: 8


# Filtrar apenas números pares
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

# Usar lambda com sorted para ordenar por tamanho de texto
palavras = ['maçã', 'uva', 'abacaxi']
ordenadas = sorted(palavras, key=lambda p: len(p))
print(ordenadas)  # Saída: ['uva', 'maçã', 'abacaxi']
