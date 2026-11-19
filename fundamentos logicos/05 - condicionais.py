nota = float(input("Informe sua nota: "))
freq = float(input("Informe a frequencia: "))


if nota >= 7 and freq >= 75:
    print(f"O aluno foi aprovado com nota {nota}!")
else:
    print("O aluno não foi aprovado!")