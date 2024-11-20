'''Entrar com três nu" meros e armazenar o maior numero na varia" vel de nome maior
(suponha números diferentes)'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

numeros = max(num1, num2, num3)

maior = numeros

print(f"Variável MAIOR: {maior}")