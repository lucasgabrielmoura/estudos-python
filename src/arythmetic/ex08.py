valorM = int(input("Coloque o valor em metros: "))

while valorM < 1:
    valorM = int(input("Coloque o valor em metros (valor acima de 1): "))

print(f"O valor {valorM}.0m equivale a: \n\n")

print(f"{valorM/1000}km\n{valorM/100}hm\n{valorM/10}dam\n{valorM*10}dm\n{valorM*100}cm\n{valorM*1000}mm")