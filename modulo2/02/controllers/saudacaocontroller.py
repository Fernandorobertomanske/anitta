from datetime import datetime
from time import sleep

def saudacao():
#a variavel hora representa o modulo interno de data e hora do python
    hora = datetime.now(tz = None)
# se a hora for maior ou igual a cinco e menor que 13
    if  hora.hour >= 5 and hora.hour <13:
        print(f'bom dia {hora.hour}: {hora.minute}')
#se a hora for maior ou igual a 13 e menor que 18
    elif hora.hour >=13 and hora.hour <18:
        print(f'boa tarde {hora.hour}: {hora.minute}')
# senao   
    else:
        print(f"good night{hora.hour}: {hora.minute}")

def cabecalho():
#polimorfismo
    
    for i in range(10):
        sleep(0.1)
        print("*")

        
def Descritivo():
        print(
    '''
1- criar
2- ler todos usuarios
3- ler um usuario pelo nome
4- alterar um usuario pelo nome
5- Deletar um usuario
''')
        