from datetime import date

anoNasceu = int(input("Coloque ano de nascimento: "))
idade = date.today().year - anoNasceu 

if idade <= 9:
    print(f"Sua idade é {idade} e você é MIRIM")
elif idade > 9 and idade <= 14:
    print(f"Sua idade é {idade} e você é INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"Sua idade é {idade} e você é JÚNIOR")
elif idade > 19 and idade <= 25:
    print(f"Sua idade é {idade} e você é SÊNIOR")
else:
    print(f"Sua idade é {idade} e você é MASTER")
