'''Entrar com o raio de um círculo e imprimir a seguinte saída:
    perimetro:
    area:
'''
import math

raio = float(input("Digite o raio do círculo: "))

perimetro = 2* math.pi * raio
area = math.pi *raio ** 2

print(f"Perímetro: {perimetro:.2f}\n"
      f"Área: {area:.2f}")