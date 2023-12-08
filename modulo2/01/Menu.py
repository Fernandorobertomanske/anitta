from calculadora import soma, subtracao, multiplicacao, divisao
from time import sleep
def menu():
    var = "sim"
    while var.lower() =="sim":
        print("qual operação matematica voce deseja fazer\nsoma\nsubtracao\nmultiplicacao\ndivisao") 
        cond =input("digite aqui")

        if cond.lower == "soma":
                n1= float(input('digite o primeiro numero'))
                n2= float(input('digite o segundo numero'))
                print(soma(n1, n2))

        elif cond.lower == "subtracao":
                    n1= float(input('digite o primeiro numero'))
                    n2= float(input('digite o segundo numero'))
                    print(subtracao(n1, n2))

        elif cond.lower == "multiplicacao":
                    n1= float(input('digite o primeiro numero'))
                    n2= float(input('digite o segundo numero'))
                    print(multiplicacao(n1, n2))

        elif cond.lower == "divisao": 
                    n1= float(input('digite o primeiro numero'))
                    n2= float(input('digite o segundo numero'))
                    print(divisao(n1, n2))        
        
        else:
            print("a operacao matematica nao existe")
              
        var =input("deseja continuar?\nsim\nnão\n >>")
        for i in range(10):
            print("#")
        sleep(1)
print("voce saiu do sistema")   

menu()