from random import choice, shuffle



n1 = input("digite seu nome")
n2 = input("digite seu nome")
n3 = input("digite seu nome")
n4 = input("digite seu nome")
n5 = input("digite seu nome")
n6 = input("digite seu nome")


poli ='*'*20
lista_nomes = [n1, n2, n3, n4, n5, n6]
sorteio = choice(lista_nomes)


if sorteio == n1:
    print(f'''o nome sorteado foi{n1}")''')

elif sorteio == n2:
    print (f'o nome sorteado foi{n2}') 

elif sorteio == n3:
    print (f'o nome sorteeado foi{n3}')       

elif sorteio == n4:
    print (f'o nome sorteado foi{n4}') 

elif sorteio == n5:
    print (f'o nome sorteeado foi{n5}')  

elif sorteio == n6:
    print (f'o nome sorteado foi{n6}') 
       
print (poli,'sorteio ',poli,'\n')
print (f'nome{sorteio} parabens voce foi sorteado')
