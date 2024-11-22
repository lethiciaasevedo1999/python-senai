'''Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de se-
gundo grau, apresentando: as duas raízes, separa os valores informados for pos- sívelfazero cálculo (deita positivo ou zero); a mensagem "Não há raízes reais", se

não for possível fazer o cálculo (deita negativo); e a mensagem "Não é equação
do segundo grau", se o valor de a for iguala zero.'''

import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))


if a == 0.0:
    print("\nNão é equação do 2º grau")
else:
    d = b**2 - 4 * a * c  # Calcula o discriminante
    
    if d >= 0.0:  # Verifica se há raízes reais
        d = math.sqrt(d)  # Calcula a raiz quadrada do discriminante
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        print(f"\nX1= {x1}\t\tX2= {x2}")
    else:
        print("\nNão há raízes reais")

