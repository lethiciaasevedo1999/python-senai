#Entrar com 10 números e imprimir a metade de cada número 

for i in range(1, 11):
    numero = int(input("Insira um número: "))
    i = numero/2
    print(f"A metade do número {numero} é {i}")
    