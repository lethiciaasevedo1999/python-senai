#1)	Faça um programa que peça um número ao usuário e informe se é Par ou Ímpar.

numero = int(input("Digite aqui o seu número: "))

if numero % 2 == 0:
    print("O número digitado é par :)")
else:
    print("O número digitado é ímpar :)")