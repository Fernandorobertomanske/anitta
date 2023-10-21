# importação otimizada

from random import choice, shuffle

n1 = input('digite o seu nome >>')
n2 = input('digite o seu nome >>')
n3 = input('digite o seu nome >>')
n4 = input('digite o seu nome >>')
n5 = input('digite o seu nome >>')
n6 = input('digite o seu nome >>')

poli = "*"*20
lista = [n1, n2, n3, n4, n5, n5, n6]
shuffle(lista)

# verde é relacionado a uma classe recurso

sorteio = choice(lista)


print(poli,"trimania de outubro", poli, "\n")
print(f"parabens{sorteio} voce ganhou 500 milhoes de reais")



