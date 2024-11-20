'''Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo 
e o quadrado do número caso ele seja negativo.'''

import math

valor1 = int(input("Digite um número: "))

if valor1 > 0:
    print(f"Raíz quadrada: {math.sqrt(valor1)}")
elif valor1 < 0:
    print(f"Quadrado: {valor1 ** 2}")

