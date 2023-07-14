nome = input("Digite valor: ")
# print(f"Valor:{nome}; Estilos:{f'{nome.upper()} - Maiúscula | {nome.lower()} - Minúscula'}; Tipo:{ 'É String' if nome.istitle() == True else 'Não é String'}") #Usando ternário

print(f"Valor:{nome}; Estilos:{f'{nome.isupper()} - Maiúscula | {nome.islower()} - Minúscula | {nome.isnumeric()} - Numérico'}; Tipo:{ type(nome) }")