from datetime import date

ano = int(input("Qual ano quer analisar? Se for o atual digite 0: "))
ano = date.today().year if ano == 0 else ano

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é BISSEXTO")
else:
    print(f"O ano {ano} não é BISSEXTO")