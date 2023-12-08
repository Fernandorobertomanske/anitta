def create(pessoa):
    with open('Banco.txt','a')as arquivo:
        arquivo.write(f'{pessoa}\n')

def ReadPessoas():
    nomes = []
    with open('Banco.txt','r')as arquivo:
         for name in arquivo:
             name = name.strip()
             nomes.append(name)
    return nomes

        
def ReadPessoa(pessoa):
    index = 0
    flag = 0
    arquivo = open('Banco.txt')
    for line in arquivo:
        index += 1
        if pessoa == eval(line)['Nome']:
            print(line)
            flag = 1
    if flag == 0:
        print('Pessoa nao encontrada')


def update(nomepessoa):
    flag = False
    
    with open('Banco.txt','r')as arquivo:
        lines = arquivo.readlines()
        for line in lines:
            if nomepessoa in lines:
                novo_nome = input('digite seu nome')
                novo_sobrenome = input('digite seu sobrernome') 
                nova_idade = input('digite sua idade >>') 
                nova_linha = f"{{'nome': '{novo_nome}','idade': '{nova_idade}'}}"
                arquivo.write(nova_linha)
                flag = True

            else:
                arquivo.write(line)
        if flag == True:
            print("cliente atualizado")
        else:
            print("cliente nao encntrado")

def delete(nomepessoa):
    flag = False
    with open('Banco.txt','r')as arquivo:
        lines = arquivo.readlines()

    with open('Banco.txt','w')as arquivo:
        for line in lines:
            if nomepessoa not in lines:
                arquivo.write(line)
            else:
                flag = True

        if flag == True:
            print("cliente deletado")
        else:
            print("cliente nao encontrado")