
def soma( a, b, ):
    print("============soma==============")
    resultado = a + b
    return resultado

def subtraçao( a, b, ):
    print("================subtracao==============")
    resultado = a - b
    return resultado

def multiplicacao(a, b,):
    print("===================multiplicacao=================")
    resultado = a * b
    return resultado


def divisao(a, b,):
    print("=======================divisao===================")
    resultado = a / b
    return resultado

print('digite o primeiro numero')
n1 = float(input())
print('digite o segundo numero')
n2 =float(input())

print(soma(n1, n2))
print(subtraçao(n1, n2))
print(multiplicacao(n1, n2))
print(divisao(n1, n2))
