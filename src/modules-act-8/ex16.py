import math

num = float(input("Digite um número fracionado: "))

print(f"Valor direto: {num:.0f} - Esse arredonda as vezes, ou seja, melhor usar trunc ou int.")
print(f"Valor usando o método trunc: {math.trunc(num)}")
print("Valor usando o objeto int: {}".format(int(num)))