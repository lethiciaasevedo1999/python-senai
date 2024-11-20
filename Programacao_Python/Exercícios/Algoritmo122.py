#Ler três números e imprimir se eles podem ou não ser lados de um triângulo.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))


if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print("Os números inseridos podem ser lados de um triângulo")
else:
    print("O números inseridos não podem ser lados de um triângulo")