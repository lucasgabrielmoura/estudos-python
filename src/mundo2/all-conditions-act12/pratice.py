nome = str(input("Nome: "))

if nome.upper() == "LUCAS":
    print("Ganhou!")
elif nome.upper() == "PEDRO" or nome.upper() == "GABRIELA" or nome.upper() == "OLIVER":
    print("Seu nome é bem popular!")
elif nome.upper() in "FERNANDO JAILSON PABLO JURANDIR":
    print("Nome diferente")
else:
    print("Perdeu!")

print(f"Tenha um bom dia {nome}!")