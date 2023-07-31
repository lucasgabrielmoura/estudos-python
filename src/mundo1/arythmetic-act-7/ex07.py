nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

while nota1 < 0 or nota2 < 0:
    if nota1 < 0:
        nota1 = float(input("Primeira nota (não pode valor negativo): "))
    elif nota2 < 0:
        nota2 = float(input("Segunda nota (não pode valor negativo): "))

print(f"Nota 1º: {nota1}\nNota 2º: {nota2}\nMédia: {(nota1+nota2)/2}")