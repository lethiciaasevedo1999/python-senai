#Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal

import math

ladoA = float(input("Digite o lado A: "))
ladoB = float(input("Digite o lado B: "))
ladoC = float(input("Digite o lado C: "))

diagonal = math.sqrt(ladoA**2 + ladoB**2 + ladoC**2)

print(f"Diagonal: {diagonal:.2f}")