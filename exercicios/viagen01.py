
import random

nome = str(input(' digite seu nome completo '))

destino01 = str(input(" digite o destino "))
destino02 = str(input(" digite o destino "))
destino03 = str(input(" digite o destino "))
destino04 = str(input(" digite o destino "))
destino05 = str(input(" digite o destino "))
destino06 = str(input(" digite o destino "))

poli ='*'*20

lista_destinos = [destino01, destino02, destino03, destino04, destino05, destino06]

sorteio = random.choice(lista_destinos)


if sorteio == destino01:

    print (f'o destino sorteado foi{destino01}')

elif sorteio == destino02:
    print (f'o destino sorteado foi{destino02}') 

elif sorteio == destino03:
    print (f'o destino sorteado foi{destino03}')       

elif sorteio == destino04:
    print (f'o nome sorteado foi{destino04}') 

elif sorteio == destino05:
    print (f'o destino sorteado foi{destino05}')  

elif sorteio == destino06:
    print (f'o destino sorteado foi{destino06}') 

       
print (poli,'sorteio ',poli,'\n')
print (f'destino {sorteio} parabens voce foi sorteado')







