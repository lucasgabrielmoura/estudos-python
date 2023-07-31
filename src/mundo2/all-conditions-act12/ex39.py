from datetime import date

ano = int(input("Ano que nasceu: "))

if date.today().year - ano > 18:
    print(f"Você tem {date.today().year - ano} em {date.today().year}")
    print(f"Seu alistamento já passou")
elif date.today().year - ano == 18:
    print(f"Você tem {date.today().year - ano} em {date.today().year}")
    print(f"Seu alistamento será esse ano!")
elif date.today().year - ano < 18:
    print(f"Você tem {date.today().year - ano} em {date.today().year}")
    print(f"Seu alistamento será daqui a {18 - (date.today().year - ano)} anos/ano!")
    print(f"Seu alistamento acontecerá em {date.today().year + (18 - (date.today().year - ano))}")