#Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o
#novo saldo, considerando o reajuste de 1%.

saldo = float(input("Digite o seu saldo: "))
porcento = saldo*1.01

print(f"Seu novo saldo é: {porcento:.2f}")

