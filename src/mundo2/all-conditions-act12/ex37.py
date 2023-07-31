

numero = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:\nHEXA - 1\nOCTAL - 2\nBINARIO - 3\n")

option = int(input("Sua opção: "))

if option == 3:
    print("\n" + bin(numero))
if option == 2:
    print("\n" + oct(numero))
if option == 1:
    print("\n" + hex(numero))