#Entrar com um número e imprimir o logaritmo desse número na base 10.

import math

numero = int(input("Digite um número: " ))
base = int(input("Digite a base: " ))

resultado = math.log(numero, base) 
print(f"O logaritmo na base {base} é: {resultado:.2f}")
