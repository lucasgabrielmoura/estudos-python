kmDaViagem = int(input("Quantos KM é a viagem? "))

if kmDaViagem > 200:
    print(f"O valor baseado em R$0,45 por KM é R${kmDaViagem * 0.45:.2f}")
else:
    print(f"O valor baseado em R$0,50 por KM é R${kmDaViagem * 0.50:.2f}")