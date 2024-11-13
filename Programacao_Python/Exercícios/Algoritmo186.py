#Entrar com quatro números e imprimir o cubo e a raiz cúbica de cada número: 

for i in range(4):
    numero = int(input("Digite um número: "))
    cubo = numero ** 3 
    raiz_cubica = numero ** (1/3)
    
    print(f"O cubo do número {numero} é {cubo}"
        f"A raíz cúbica do numero {numero} é {raiz_cubica:.2f}")
