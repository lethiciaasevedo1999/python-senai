'''Entrar com um número e imprimir a seguinte saída: 
    número: 
    quadrado:
    raíz quadrada: 
'''

import math

numero = int(input("Digite um número: "))

print(f"Número: {numero}\n"
      f"Quadrado: {numero **2}\n"
      f"Raíz quadrada: {math.sqrt(numero)}")