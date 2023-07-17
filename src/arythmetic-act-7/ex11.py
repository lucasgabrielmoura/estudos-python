base = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
valorM2Default = 15

print("Sua parede tem dimensão de {}x{} e sua área é {}m2".format(base,altura, base*altura))
print("Para pintar essa parede será necessário {}l".format((altura*base)/valorM2Default)) #Regra de 3 usando variáveis