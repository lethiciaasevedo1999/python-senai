'''Criar um algoritmo que receba um número real, calcular e imprimir:
- a parte inteira do número
- a parte fracionária do número
- o número arredondado'''

import math 

numero = float(input("Digite o número: "))

print(f"Parte inteira: {math.trunc(numero)}\n"
      f"Parte fracionária: {math.modf(numero)}\n"
      f"Número arredondado: {math.ceil(numero)}")




