from random import shuffle

n1 = str(input("Aluno 1ª: "))
n2 = str(input("Aluno 2ª: "))
n3 = str(input("Aluno 3ª: "))
n4 = str(input("Aluno 4ª: "))

lista = [n1,n2,n3,n4]

shuffle(lista)

print(lista)