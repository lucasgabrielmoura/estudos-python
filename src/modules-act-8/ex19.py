from random import randint

n1 = str(input("Aluno 1ª: "))
n2 = str(input("Aluno 2ª: "))
n3 = str(input("Aluno 3ª: "))
n4 = str(input("Aluno 4ª: "))

lista = [n1,n2,n3,n4]

sorteador = randint(0, lista.__len__() - 1)
print(f"O aluno sorteado foi {lista[sorteador]} do número {sorteador+1}")