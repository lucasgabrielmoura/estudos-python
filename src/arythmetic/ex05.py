
valor = int(input("Digite o valor: "))

while valor <= 1:
    valor = int(input("Digite o valor acima de 1: "))
    
print(f"Analisando o valor: {valor} \nAntecessor: {valor-1} \nSucessor: {valor+1}")