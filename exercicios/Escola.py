nome =  str(input('nome do aluno'))
idade = str(input('idade do aluno'))
anoletivo = str(input(' ano letivo do aluno'))
materia = str(input('materia do aluno'))
nota1 = float(input('primeira nota'))
nota2 = float(input('segunda nota'))

media = (nota1 + nota2)/2


lista = [nome, idade, anoletivo, materia, nota1, nota2]
print(lista)

nota = 7.0

if media > 7.0:
    print('parabens voce foi aprovado')

elif media < 7.0:
    print('voce foi reprovado')

else:
    print(' a media é exatamente 7.0')


poli = '='*20
print(poli , 'media' , poli)

print(f'''
o nome do aluno é
a idade do aluno é      
o ano letivo é
a materia foi                  
a primeira nota foi
a segunda nota foi   
''')






