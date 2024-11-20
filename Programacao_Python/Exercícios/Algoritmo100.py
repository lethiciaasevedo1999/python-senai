'''Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o nú-
mero formado pelos algarismos que estão nas casas das unidades de milhar e das centenas.'''

numero = input("Digite um número inteiro de 4 casas deciamais: ")
numero = numero[0:2]

if int(numero) % 4 == 0:
    print(f"O número {numero} é múltiplo de 4")
else:
    print(f"O número {numero} não é múltiplo de 4")
