#Entrar com dois números e imprimir o menor numero (suponha números diferentes).

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 < num2:
    print(f"Número menor: {num1}")
else:
    print(f"Número menor: {num2}")