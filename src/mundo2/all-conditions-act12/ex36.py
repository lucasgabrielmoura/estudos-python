valorAPegar = float(input("Valor do empréstimo: "))
salario = int(input("Salário a pagar: "))
prestacao = int(input("Prestações: "))

print(f"Para pegar um emprestimo de R${valorAPegar} em {prestacao} anos de prestação, será R${valorAPegar / (prestacao*12):.2f}")

checadorDeSalario = ((valorAPegar / (prestacao*12)) * 100) / salario

if checadorDeSalario > 30:
    print("Seu pedido de empréstimo foi NEGADO")
else:
    print("Seu pedido de empréstimo foi APROVADO!")