'''Ler três números, os possíveis lados de um triângulo, e imprimira classificação 
 segundo os lados.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    if num1 == num2 and num1 == num3:
        print("Triângulo equilátero")
    elif num1 == num2 and num1 == num3 and num2 == num3:
        print("Triângulo  isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("As medidas inseridas não podem ser lados de um triângulo")