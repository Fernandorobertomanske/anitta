from controllers.PessoaController import create, ReadPessoa, ReadPessoas, update, delete

from .Interatation import Interacao
# possibilidade de interação entre usuario e sistema
#tudo que é relacionado com usuario fica dentro da pastra view

def menu():
    var ='sim'
    while var == "sim":
        Interacao()
    
        cond = int(input('digite aqui>>'))
        match(cond):
            case 1:
                    pessoa = {}
                    pessoa['Nome'] = input('digite seu nome')
                    pessoa['Sobrenome'] = input('digite saeu sobrenome')
                    pessoa['Idade'] = input('digite sua idade')
                    create(pessoa)
            case 2:
                        
                    print("Digite o nome da pessoa que deseja saber os dados")
                    pessoa = input('digite o nome aqui')

                    ReadPessoas(pessoa)
            
            case 4:
                print("voce escolheu alterar um usuario segue a listaatualizada de nomes")
                print(ReadPessoa())
                print()
                nome = input("digite o nome que deseja alterar")
                update(nome)
                pass
            case 5:
                nome = input('digite o nome da pessoa que deseja deletar')
                delete(nome)
                
    var = input("deseja continuar? sim nao")


        


