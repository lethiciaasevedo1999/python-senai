'''Efetuará leitura de cinco números inteiros diferentes e identificar o maior e o menor valor.'''


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))
num4 = int(input("Digite outro número: "))
num5 = int(input("Digite outro número: "))

numeros = [num1, num2, num3, num4, num5]

numeros.sort()

print(f"Maior número: {numeros[4]}\n"
      f"Menor número: {numeros[0]}")
