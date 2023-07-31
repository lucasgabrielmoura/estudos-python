nome = str(input("Digite seu nome completo: ")).strip()

print(f"Analisando nome...")
print(f"Seu nome em caixa alta: {nome.upper()}")
print(f"Seu nome em caixa baixa: {nome.lower()}")
print(f"Seu nome em tem: {len(nome) - nome.count(' ')} letras")
print(f"Seu primeiro nome é {nome.split()[0]} e tem: {len(nome.split()[0])} letras")