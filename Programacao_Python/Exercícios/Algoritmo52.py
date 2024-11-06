'''Entrar com o lado de um quadrado e imprimir:
    perímetro:
    area:
    diagonal:
'''

import math

ladoQuadrado = float(input("Digite o lado do quadrado: "))

perimetro = 4 * ladoQuadrado
area = ladoQuadrado ** 2
diagonal = ladoQuadrado * math.sqrt(2)

print(f"Perímetro: {perimetro:.2f}\n"
      f"Área: {area:.2f}\n"
      f"Diagonal: {diagonal:.2f}")