# Testando condicionais e Funções #

a: int = 0
b: int = 1

def fibonnaci(quant: int):

    global a, b

    for i in range (quant):
        print(f"{a} {b}")
        a = a + b
        b = b + a


fibonnaci(10)
# -------------//-------------- #