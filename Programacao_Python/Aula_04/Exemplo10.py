#Calculando a raíz cúbica com funções

def raizCubica(numero):
    raizCubica = numero**(1/3)
    return raizCubica


resultado = 27**(1/3)
print(f"Raíz cubica de 27: {resultado}")

print(f"Raíz cubica de 27: {raizCubica(27)}")