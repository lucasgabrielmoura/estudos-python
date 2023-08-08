for i in range (1,10):
    print(f" Testando incremento com range de 1 a 10: {i}")
print("-------------------")

for i in range (10, 1, -1):
    print(f" Testando decremento com range de 10 a 1: {i}")

print("-------------------")

for i in range (1, 10, 2):
    print(f" Testando incremento de +2 com range de 1 a 10: {i}")

print("-------------------")

for i in range (10):
    print(f" Testando incremento com range de 0 a 10: {i}")

inicio = 0
fim = 100
passo = 10

for i in range (inicio, fim+1, passo):
    print(f" Testando incremento de 10 com range de 0 a 100: {i}")