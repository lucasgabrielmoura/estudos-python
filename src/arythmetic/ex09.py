valorTabuada = int(input("Digite um valor maior que 0: "))

while valorTabuada <= 0:
    valorTabuada = int(input("Digite um valor maior que 0: "))



def tabuada(valor):
    print("-----------")
    for i in range(10):
        print(f"{valor} x {i+1} = {valor*(i+1)}")
    print("-----------")


tabuada(valorTabuada)