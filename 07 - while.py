# Inicializamos a variável de controle
contador = 1

# O loop executa ENQUANTO o contador for menor ou igual a 5
while contador <= 5:
    print(f"Execução número: {contador}")
    
    # IMPORTANTE: Incrementamos o contador para evitar um loop infinito
    # É o equivalente a 'contador = contador + 1'
    contador += 1 



# Cria um loop que, por padrão, nunca terminaria sozinho
while True:
    resposta = input("Digite 'sair' para encerrar o programa: ")
    
    # Condição de parada
    if resposta.lower() == 'sair':
        print("Encerrando o programa...")
        break # Interrompe o loop imediatamente
        
    print(f"Você digitou: {resposta}. Vamos continuar!")



