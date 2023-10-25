#lista vazia
#indice

n1 = int(input(" digite o numero de vezes que deseja pedir a nota do aluno"))
lista = []

#extrutura de repetição
#inicio I fim 3
#indice
#imutavel
#dinamico

for i in range(n1):
    nota = float(input("digite seu nome:"))
    lista.append(nota)

media = sum(lista) /(lista)
# 10 + 3 + 7 + 8 + 9 / 5

# 1    2   3   4
print(media)