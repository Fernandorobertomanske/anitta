print(' digite seu nivel de experiencia')
nivel = int(input('digite seu nivel entre (1 ate 10)'))
mensagem = None
#estrutura de controle de fluxo condicional

if nivel < 1:
   mensagem = f'voce digitou um numero invalido{nivel}'
   print(mensagem) 

elif nivel <= 3:
   mensagem = 'voce esta no nivel iniciante'
   print(f'o seu nivel é{mensagem}')

elif nivel >3 <=6:
   mensagem = 'voce esta no nivel intermediario'
   print(f' o seu nivel é {mensagem}')

elif nivel >6 <=10:
   mensagem = 'voce esta no nivel avançado'
   print(f' o seu nivel é {mensagem}')
   