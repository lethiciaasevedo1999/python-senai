'''Entrar com três números e armazená-los em três variáveis com os seguintes no-
mes maior, intermediário e menor (suponha numeros diferentes)'''


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

numeros = [num1, num2, num3]
numeros.sort()


print(f"Maior: {numeros[2]}\n"
      f"Intermediário: {numeros[1]}\n"
      f"Menor: {numeros[0]}")