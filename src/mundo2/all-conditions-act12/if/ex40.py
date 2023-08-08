nota1 = float(input("Nota 1º: "))
nota2 = float(input("Nota 2º: "))
media = ((nota1 + nota2) / 2)

if media >= 7.0:
    print(f"Aluno foi aprovado com média: {media}")
elif media > 5.0 and media < 6.9:
    print(f"Aluno tá em recuperação com média: {media}")
else:
    print(f"Aluno não passou com média: {media}")