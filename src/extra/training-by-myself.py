# Testando condicionais e Funções #

a: int = 0
b: int = 1

def fibonnaci(quant: int):

    global a, b

    for i in range (quant):
        print(f"{a} {b}")
        a = a + b
        b = b + a
        if(i == 0):
            print("start")
        elif(i == 4):
            print("middle")
        elif(i+1 == quant):
            print("end")
        else:
            print("|")

fibonnaci(10)
# -------------//-------------- #

# Testano variáveis #