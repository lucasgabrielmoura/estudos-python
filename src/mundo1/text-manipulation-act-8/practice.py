frase = "Curso de Python"
print(frase[0]) #Pegando uma letra pois string como qualquer outra linguagem é tratado como Array/Lista
print(frase[0:5]) #Pegando do index 0 até o 5 trazendo a palavra Curso
print(frase[0:14:2]) #Do index 0 até o 14 pulando de 2 em 2, ou seja, pulando de 2 em 2 caracteres
print(frase[:5]) #Mesma coisa que print(frase[0:5])
print(frase[5:]) #Do 5 até o final (bom pra quando não sabe o final)
print(frase[5::3]) #Do 5 até o final pulando 3 caracteres

#Analisando String

print(len(frase)) #Diz o tamanho da string
print(frase.count("o")) #Conta a quantidade de letras ou palavras em tal frase
print(frase.count("o",0,5)) #O mesmo de cima só que com começo e fim específico
print(frase.find("de")) #Procura e fala aonde começa essa palavra ou frase
print(frase.find("Android")) #Trás -1 pois não encontra
print('Curso' in frase) #Ele serve para checar e trazer true ou false
print(frase.replace('Python', 'Android')) #Passa o valor antigo e o valor novo que vai ser colocado no lugar
print(frase.upper()) #Deixa em caixa alta toda frase
print(frase.lower()) #Deixa em caixa baixa toda frase
print(frase.capitalize()) #Todos caracteres para minusculo e o primeiro em maiúsculo
print(frase.title()) #Ele vai pegar todo começo de palavra e por em maiúsculo

frase2 = "   Aprenda Python   "

print(frase2.strip()) #Elimina os espaços descartáveis.
print(frase2.rstrip()) #Elimina os espaços da direita.
print(frase2.lstrip()) #Elimina os espaços da esquerda.
print(frase2.split()) #Ele corta em cada espaço transformando em lista cada pedaço.
print(frase2.split(),'-'.join(frase)) #Ele pega as listas criadas e bota entre eles os traços.

print("""\nAssim que o dia amanheceu
Lá no mar alto da paixão
Dava pra ver o tempo ruir
Cadê você? Que solidão
Esquecera de mim
Enfim, de tudo o que há na terra
Não há nada em lugar nenhum
Que vá crescer sem você chegar
Longe de ti tudo parou
Ninguém sabe o que eu sofri""")