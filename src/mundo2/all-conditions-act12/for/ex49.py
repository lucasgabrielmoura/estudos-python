numero = int(input("Digite a tabuada que quer ver: "))

for valor in range(1, 10):
    print(f"{numero} x {valor}: {numero*valor}")