nome = str(input("Digite seu nome: ")).strip()
nomeDividido = nome.split()

print(f"O primeiro nome: {nomeDividido[0]}")
print(f"O último nome: {nomeDividido[len(nomeDividido) - 1]}")

print()