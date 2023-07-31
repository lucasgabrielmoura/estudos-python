n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

menor:int = n1
maior:int = n1

lista = [n1,n2,n3]

for i in range(len(lista)):
    menor = lista[i] if lista[i] < menor else menor
    maior = lista[i] if lista[i] > maior else maior

print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")