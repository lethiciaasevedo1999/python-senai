'''Ler três números, os possíveis lados de um triângulo, e imprimira classificação se-
gundo os ângulos.'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))


if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    
    if num1 > num2 and num1 > num3:
        maior = num1 ** 2
        lados = num2 ** 2 + num3 ** 2
    elif num2 > num3:
        maior = num2 ** 2
        lados = num1 ** 2 + num3 ** 2
    else:
        maior = num3 ** 2
        lados = num1 ** 2 + num2 ** 2

    
    if maior == lados:
        print("Triângulo Retângulo")
    elif maior > lados:
        print("Triângulo Obtusângulo")
    else:
        print("Triângulo Acutângulo")
else:
    print("Os números fornecidos não formam um triângulo.")

    