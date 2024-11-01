#Calculando númros pares e ímpares

numero = int(input("Digite um número: "))

resultado = numero % 2 != 0
print(resultado)

if resultado == True:
    print("Número ímpar")
else:
    print("Número par")