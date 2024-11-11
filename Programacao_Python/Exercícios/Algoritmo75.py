'''Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e
imprimir:
- o peso da pessoa em gramas
- novo peso em gramas se a pessoa engordar 12%'''

import math 

peso = float(input("Digite o seu peso: "))
peso = math.trunc(peso)
pesoGramas = peso * 1000
novoPeso = peso * 12 /100


print(f"Peso em gramas: {pesoGramas}\n"
      f"Novo peso: {novoPeso + peso:.2f}")

