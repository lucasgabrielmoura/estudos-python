nome = input("Digite valor: ")
print(f"Valor:{nome}; Estilos:{f'{nome.upper()} - Maiúscula | {nome.lower()} - Minúscula'}; Tipo:{ 'É String' if nome.istitle() == True else 'Não é String'}")