#======= Formas de usar Operações Aritméticas =======#

nome = str(input("Coloque seu nome: "))

print("Prazer em te conhecer {:20}! - Utilizando manipulação dentro da String".format(nome))
print("Prazer em te conhecer {:>20}! - Alinhando pro final em 20 caracteres string".format(nome))
print("Prazer em te conhecer {:<20}! - Alinhando pro começo em 20 caracteres string".format(nome))
print("Prazer em te conhecer {:^20}! - Alinhando pro meio em 20 caracteres string".format(nome))
print("Prazer em te conhecer {:=^20}! - Alinhando e preenchendo espaços com =, porém pode ser qualquer outra coisa".format(nome)) #Esse end serve para não quebrar a linha
print(f"Prazer em te conhecer {nome:=^20}! - Alinhando e preenchendo espaços com =, porém pode ser qualquer outra coisa (funcionando sem format)")