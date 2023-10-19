from random import choice, shuffle
# importação otimizada, shuffle


n1 = input('digite seu nome') 
n2 = input('digite seu nome') 
n3 = input('digite seu nome') 
n4 = input('digite seu nome') 
n5 = input('digite seu nome') 
n6 = input('digite seu nome') 

poli ='*'*20
lista = [n1, n2, n3, n4, n5, n6]
shuffle(lista)

sorteio = choice(lista)

print(poli,'trimania de outubro',poli,'\n')
print(f'parabens{sorteio} voce ganhou 500 milhoes de reais')