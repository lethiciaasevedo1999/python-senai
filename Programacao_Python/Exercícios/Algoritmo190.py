'''Entrar com um nome, idade e sexo de 20 pessoas. Imprimir o nome se a pessoa for
do sexo masculino e tiver mais de 21 anos.'''



for i in range(1, 4):
    nome = (input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    print("Qual o seu sexo? ")
    sexo = input("Digite 'f' para feminino e 'm' para masculino:  ")

    if sexo == "m" and idade > 21:
        print(nome)