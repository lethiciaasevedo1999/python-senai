'''Entrar com dois números e imprimi-los em ordem crescente (suponha números
diferentes).'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

numerosOrdenados = [num1, num2]
numerosOrdenados.sort()

print(numerosOrdenados)