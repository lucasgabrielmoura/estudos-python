numeros:list = []
soma:int = 0

for i in range(0, 5):
    numeros.append(int(input(f"Escolha o {i+1}º: ")))
    if numeros[i] % 2 == 0:
        soma += numeros[i]

print(f"A soma deu: {soma}")
