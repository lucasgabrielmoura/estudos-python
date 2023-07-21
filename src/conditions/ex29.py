velocidadeValidator = int(input("Qual a velocidade do carro? "))

if velocidadeValidator > 80:
    print(f"Você excedeu a velocidade, e foi MULTADO no valor de R${(velocidadeValidator-80)*7}")
else:
    print(f"Seguindo na velocidade permitida.")