#Entrar com 10 números e imprimir o quadrado de cada número


for i in range(1,11):
    numero = int(input("Digite um número: "))
    i = numero ** 2
    print(f"O quadrado do número {numero} é {i}")