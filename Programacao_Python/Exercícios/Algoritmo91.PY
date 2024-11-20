'''Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; 
caso o resultado seja maior que 10, apresentá-lo.'''

valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))

soma = valor1 + valor2

if soma > 10:
    print(soma)