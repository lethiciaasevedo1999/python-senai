'''Ler um número e, se ele for positivo, imprimir seu inverso; caso contrário, impri-
mir o valor absoluto do número.'''

numero = int(input("Digite um número: "))

if numero > 0 :
    numero = int(str(numero)[::-1])
    print(numero)
else: 
    print(numero)