'''Entrar com três números e imprimi-los em ordem decrescente (suponha números
diferentes).'''


num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

numeros = [num1, num2, num3]
numerosCrescentes = sorted(numeros, reverse=True)

print(f"Números em ordem crescente: {numerosCrescentes}")