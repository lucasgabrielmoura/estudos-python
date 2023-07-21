import random
import time


print(f"\n{'':=^50}")
print("Vou escolher um número de 0 a 5, tente advinhar!")
print(f"{'':=^50}")

numeroEscolhido = int(input("\nQual número eu pensei? "))

while numeroEscolhido > 5 or numeroEscolhido < 0:
    numeroEscolhido = int(input("\nQual número eu pensei(Apenas números nessa faixa)? "))

print("\nPROCESSANDO...\n")
time.sleep(1)

numeroPensado = random.randint(0,5)

if numeroEscolhido == numeroPensado:
    print(f"Isso mesmo, o número escolhido foi {numeroEscolhido} e o que eu pensei foi {numeroPensado}!!")
else:
    print(f"Errado, o número escolhido foi {numeroEscolhido} e o que eu pensei foi {numeroPensado}!!")
