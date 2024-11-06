#Calculando raíz quadrada de um número complexo

import cmath

valor = 16

resultado = cmath.sqrt(16)
print(f"Raíz quadrada de 16(complexo): {resultado}")

#cmath vai possibilitar trabalhar com números negativos
resultado = cmath.sqrt(-16)
print(f"Raíz quadrada de -16(complexo): {resultado}")

resultado = 25 + cmath.sqrt(-16)
print(f"Raíz quadrada de 16(complexo): {resultado}")