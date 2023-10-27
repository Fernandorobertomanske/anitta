from datetime import datetime 
from time import sleep

situacao = "Reprovado"
while situacao.capitalize() == "Reprovado":
# Bloco 1 saudação
    hora = datetime.now(tz=None)
    if hora.hour >= 5 and hora.hour <13:    
            print(f" bom dia !! agora são{hora.hour}")
    elif hora.hour >= 13 and hora.hour < 18:
            print(f"boa tarde !! agora são {hora.hour}: {hora.minute})")            
    else:
            print(f" boa noite !! agora são {hora.hour}: {hora.minute}")

        # bloco 2
    nome = input(" digite seu nome >>")
    sobrenome = input(" digite seu sobrenome >>")
    idade = int(input(" digite sua idade >>"))
    listaNotas = []

    for i in range( 1, 7):
        nota = float(input(f"digite a nota {i}>>"))
        listaNotas.append(nota)
        media = sum(listaNotas) / len(listaNotas) 

        # bloco 4

    if media < 7.0:
            situaçao = " Reprovado"
            print(f" ola {nome}infelismente voce foi reprovado com a media de {media}")
            print(" tente novamente e tenha boa sorte")
    elif media >=7.0:
            situacao = " aprovado"
            for i in range(10):
                sleep(1)
                print(' * ')
            print(" parabens voce foi bagual") 
            print(f"{nome} voce foi aprovado e ira para um novo desafio sua media foi{media}")
    Aluno = {
                'Nome': nome,
                'SobreNome': sobrenome,
                'Idade': idade,
                'Notas': listaNotas,
                'Situacao': situacao
            }

    print("voce deseja saber todas as informacoes do aluno?")
    var = input("Sim\n Nao\n>>")

    if var.capitalize() == "Sim":
        print(f'''
Nome : {Aluno['Nome']}
SobreNome : {Aluno['SobreNome']}
Idade : {Aluno['Idade']}
lista Notas : {Aluno['Notas']}
Situacao : {Aluno['Situacao']}
''')







  
