'''Ler um número e imprimir se ele é positivo, negativo ou nulo.'''

numero = int(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo")
elif numero < 0:
    print(f"O número {numero} é negativo")
else:
    print(f"O número {numero} é nulo")