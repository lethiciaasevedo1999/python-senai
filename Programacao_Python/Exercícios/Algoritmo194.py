'''Criar um algoritmo que leia um número e imprima todos os números de 1 até o 
número lido e o seu produto. Exemplo: 

Número: 3                         Saída: 1 2 3 
                                      6                                       '''

import math

numero = int(input("Digite o número: "))

produto = 1

for i in range (1, numero + 1):
    print(i)
    produto *= i

print(f"Produto: {produto}")
