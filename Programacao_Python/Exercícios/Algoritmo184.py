#Entrar com 8 números e, para cada número, imprimir o logarítmo desse número na base 10

import math

for i in range(1, 9):
    numero = int(input("Digite um número: "))
    i = math.log10(numero)
    
    print(f"O logarítmo é {i:.2f}")