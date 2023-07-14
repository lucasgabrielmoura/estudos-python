dinheiro = int(input("Bote o dinheiro que você tem: R$"))

while dinheiro <= 0:
    dinheiro = int(input("Bote o dinheiro que você tem (Não pode ser 0 ou negativo): R$"))

print("Seu R${} se tornou U${:.2f}".format(dinheiro, dinheiro/4.81)) #Aplicando para que float tenha só 2 casas decimais após a vírgula.