'''Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante,
co-secante e co-tangente deste ângulo.'''

import math

angulo = float(input("Digite um ângulo em graus: "))

angulo = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)
secante = 1 / cosseno
co_secante = 1 / seno
co_tangente = 1 / tangente

print(f"Ângulo: {angulo:.2f}\n"
      f"Seno: {seno:.2f}\n"
      f"Cosseno: {cosseno:.2f}\n"
      f"Tangente: {tangente:.2f}\n"
      f"Secante: {secante:.2f}\n"
      f"Co-Secante: {co_secante:.2f}\n"
      f"Co-Tangente: {co_tangente:.2f}\n"
      )