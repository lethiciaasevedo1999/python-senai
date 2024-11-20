'''Construir um algoritmo que leia dois números e efetue a adição. Caso o valor so-
mado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;

caso o valor somado seja menor ou igual a 20, este deverá ser apresentado sub-
traindo-se 5.'''

valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))

resultado = valor1 + valor2

if resultado > 20:
    print(resultado + 8)
elif resultado <= 20:
    print(resultado - 5)