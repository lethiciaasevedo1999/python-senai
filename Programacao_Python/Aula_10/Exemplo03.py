#Cálculo raiz quadrada com funções

import math

def somar (a, b):
     total = a + b
     return total
     
valor01 = int(input("Digite um número: "))
valor02 = int(input("Digite outro número: "))

numero = somar(valor01, valor02)

raiz = math.sqrt(numero)
print(f"Raíz quadrada: {raiz:.2f}")