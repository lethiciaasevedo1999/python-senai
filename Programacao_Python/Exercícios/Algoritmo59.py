#Entrar com os valores dos catetos de um triângulo retângulo e imprimir a hipotenusa

cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

import math

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"O calor da hipotenusa é: {hipotenusa:.2f}")