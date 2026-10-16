# 1. Função simples sem argumentos e sem retorno
def saudar_usuario():
    print("Olá! Seja bem-vindo ao sistema.")

# 2. Função com argumentos obrigatórios e retorno de valor
def somar(a, b):
    # O comando return devolve o resultado para quem chamou a função
    return a + b

# 3. Função com argumentos opcionais (Default Arguments)
# Se 'mensagem' não for passada, ela usará o valor padrão "Até logo"
def despedida(nome, mensagem="Até logo"):
    print(f"{mensagem}, {nome}!")

# --- Testando as funções ---
saudar_usuario()

resultado = somar(10, 15)
print(f"O resultado da soma é: {resultado}")

# Usando o argumento padrão
despedida("Carlos") 
# Substituindo o argumento padrão e usando argumentos nomeados (Keyword Arguments)
despedida(mensagem="Bom final de semana", nome="Ana")



# Recursividade: Função que chama a si mesma

def fatorial(n):
    # 1. Caso Base: O fatorial de 0 ou 1 é sempre 1
    if n == 0 or n == 1:
        return 1
    
    # 2. Caso Recursivo: N multiplicado pelo fatorial de (N - 1)
    else:
        return n * fatorial(n - 1)

# --- Testando ---
# Explicação de fatorial(4):
# 4 * fatorial(3) -> 4 * (3 * fatorial(2)) -> 4 * 3 * (2 * fatorial(1))
# Quando chega em fatorial(1), retorna 1 e resolve a conta de trás para frente: 4 * 3 * 2 * 1 = 24
numero = 4
print(f"O fatorial de {numero} é {fatorial(numero)}")
