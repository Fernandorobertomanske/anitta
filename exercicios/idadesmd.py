nome01 = input('digite o seu nome ')
idade01 = float(input(' digite a sua idade'))

nome02 = input(' digite o seu nome') 
idade02 = float(input(' digite a sua idade'))

nome03 = input(' digite o seu nome')
idade03 = float(input(' digite a sua idade'))

media_idades = (idade01 + idade02 + idade03)/3
nomes = [nome01, nome02, nome03]
idades = [idade01, idade02, idade03]

categoria = None

if media_idades <18:
    categoria = 'menor de 18'

elif media_idades >=18 <30:
    categoria = ' esta entre 18 e 29 '

elif media_idades >=30 <40:
    categoria = ' esta entre 30 e 39 '       

elif media_idades >=40 <50:
    categoria = ' esta entre 40 e 50 '       

print('a lista de nomes digitada é', nomes)
print('a lista de idades digitada é', idades)
print(' a media das idades digitadas é', categoria)
print("media_idades")