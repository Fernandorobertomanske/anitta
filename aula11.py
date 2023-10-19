texte = input('digite alguma coisa')

# função com condição com responsabilidade unica

print('tem espaço?', texte.isspace())
print('contem caractere numerico?', texte.isnumeric())
print('contem caractere alfabetico', texte.isalpha())
print('contem caractere alfanumerico?', texte.isalnum())