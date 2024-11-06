'''Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:
    perímetro
    area
    diagonal
'''

import math

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))

perimetro = 2*(base + altura)
area = base * altura
diagonal = math.sqrt(base**2 + altura**2)

print(f"Perímetro: {perimetro}\n"
      f"Área: {area}\n"
      f"Diagonal: {diagonal}")

