'''Calcular e apresentar o valor do volume de uma lata de óleo, utilizando a fórmu-
la:volume = 3.14159 * R2 * altura.'''

import math

altura = float(input("Digite a altura: "))
raio = float(input("Digite o raio da lata: "))

volume = math.pi * pow(raio, 2) *altura

print(f"O volume da lata é: { volume:.2f}")


