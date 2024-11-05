#Calculando o IMC

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#FORMA ERRADA
imc = peso/(altura*altura)
print(f"Seu IMC é {imc :.2f}")

#FORMA CERTA
imc = peso/(altura*altura)
print(f"Seu IMC é {imc :.2f}")
#OU
imc = peso/altura**2
print(f"Seu IMC é {imc :.2f}")