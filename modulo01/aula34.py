var = 'sim'
#lower( transforma a string em minuscula)
# upper( transforma a string em maiusculo)


while var.capitalize() == 'Sim':
    n1 =int(input("digite um numero"))
    n2 =int(input("digite um numero"))
    soma = n1 + n2
print(f" o primeiro numero é{n1}n\o segundo numero é{n2}n\a soma é{soma}")

print(" deseja fazer um novo calculo")
var = int(input("digite 1 para continuar\ndigite 0 para sair"))

print("voce saiu do sistema")
