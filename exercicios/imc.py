nome = input("digite seu nome")
altura = float(input('digite a altua em metros'))
peso = float(input("seu peso em kg"))

IMC = peso/(altura**2)

categora = None

if  IMC < 18.5:
    categoria = "abaixo do peso"

elif IMC >= 24.9:

    categoria = "peso normal"

elif IMC >= 29.0:
    categoria = "acima do peso"

print("ola", nome, "segundo os calculos o seu IMC esta", categoria)