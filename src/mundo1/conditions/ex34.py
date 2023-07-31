salario = int(input("Qual o salário: "))

if salario >= 1250:
    print(f"Aplicando o aumento de 10% o salário saiu de R${salario:.2f} para R${(salario * 0.1)+salario:.2f}")
else:
    print(f"Aplicando o aumento de 15% o salário saiu de R${salario:.2f} para R${(salario * 0.15)+salario:.2f}")

