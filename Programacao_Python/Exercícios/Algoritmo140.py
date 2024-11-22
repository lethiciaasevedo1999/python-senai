'''Um restaurante faz uma promoção semanal de descontos para clientes de acordo
com as iniciais do nome da pessoa. Criar um algoritmo que leia o primeiro nome
do cliente, o valor de sua conta e se o nome iniciar com as letras A, D, M ou 5, dar
um desconto de 30%. Para o cliente cujo nome não se inicia por nenhuma dessas
letras, exibir a mensagem "Que pena. Nesta semana o desconto não é para seu
nome; mas continue nos prestigiando que sua vez chegara".'''

nome = input("Insira seu nome: ")
primeiraLetra = (nome[0])
valorConta = float(input("Digite o valor da sua conta: "))

if primeiraLetra == "A" or primeiraLetra == "a" or primeiraLetra == "D" or primeiraLetra == "d" or primeiraLetra == "M" or primeiraLetra == "m" or primeiraLetra == "S" or primeiraLetra == "s":
    print(f"Parabéns, você ganhou um desconto de 30% !\n"
          f"Valor da conta: R$ {valorConta}\n"
          f"Valor final -30% : {valorConta - ((30 * valorConta / 100)):.2f}")
else:
    print("Que pena. Nesta semana o desconto não é para o seu nome,\n"
          "mas continue nos prestigiando que sua vez chegará :)\n"
          f"Valor da conta: R$ {valorConta}")