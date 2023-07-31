quantosAnosCarro = int(input("Quantos anos tem seu carro: "))

#Condição normal
if quantosAnosCarro >= 5:
    print("KM deve ser checada")
else:
    print("Tá tranquilo, pode comprar")

#Condição ternária

print('KM deve ser checada' if quantosAnosCarro >= 5 else 'Tá tranquilo, pode comprar')