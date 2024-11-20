#Entrar com três números e imprimir o maior número (suponha números diferentes).

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

numeros = [num1, num2, num3]
numeroMaior = numeros.sort()

print(f"Número maior: {numeroMaior[0]}")