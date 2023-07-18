import math
import random

from math import sqrt, floor

num = int(input("Digite um número: "))

raiz = sqrt(num)
raizRaiz = num ** (1/2)

print(f"\nRaiz com import: {floor(raiz)}\nRaiz a mão: {math.ceil(raizRaiz)}")

numRandom = random.randint(0, 10)

print("\n\n\nNúmero Random: {}".format(numRandom))