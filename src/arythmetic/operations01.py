n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

print(f"A soma dos valores com forma mais rápida: {n1+n2}", end='') #Jeito mais rápido
print("A soma dos valores com format: {}".format(n1+n2)) #Format padrão
print("A soma dos valores \n {0} + {1} é {2}".format(n1,n2,n1+n2), end='') #Colocando com numero com \n para quebrar linha e end='' no final para não quebrar e pode se qualquer coisa no end='---'
print("A soma dos valores {} + {} é {}".format(n1,n2,n1+n2)) #Sem número mais em ordem