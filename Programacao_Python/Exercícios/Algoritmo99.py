'''Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa das
centenas é par ou ímpar.'''

numero = input("Digite um número inteiro de 3 casas deciamais: ")
numero_str = str(numero[2])


if int(numero_str) % 2 == 0:
    print(f"O número {numero[2]} é par")
else:
    print(f"O número {numero[2]} é ímpar")