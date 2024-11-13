# Imprimir o quadrado dos números de 1 até 10

import math 

for i in range(1 , 21):
    resultado = math.pow(i , 2)
    print(f"O quadrado do número {i} é {resultado:.0f}")