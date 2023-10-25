nota = int(input('digite o numero da tabuada que eeseja saber >'))

for c in range(1, 11):
    print("{} x {} = {} ".format(nota, c, nota*c))