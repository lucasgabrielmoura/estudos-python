dias = int(input("Quantos dias alugados: "))
km = int(input("Quantos KMs rodados: "))
valorKm:float = 0.15
valorDia:int = 60

print(f"O valor final a pagar é de: R${(dias*valorDia)+(km*valorKm)}")