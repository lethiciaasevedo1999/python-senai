#Trabalhando com estruturas de repetição 

'''Criar um algoritmo que entre com cinco números e imprimir o quadrado de cada
número.'''

import math

for i in range(1, 6):
    numero = int(input("Digite um número: "))
    resultado = math.pow(numero, 2)
    print(f"O quadrado do número {numero} é: {resultado:.2f}")
    