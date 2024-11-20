'''Criar o algoritmo que deixe entrar com dois números e imprimir o quadrado do
menor número e a raiz quadrada do maior número, se for possível.'''

import math

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"Raíz quadrada do menor número: {math.sqrt(num1):.2f}")
    print(f"Quadrado do maior número: {num2 ** 2}")