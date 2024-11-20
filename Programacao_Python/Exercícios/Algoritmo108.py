#Idem ao anterior, porém considerar: JOSÉ, José ou josé.

nome = input("Digite o seu nome: ")
primeiroNome = str(nome[0:4])


if primeiroNome == "José " or primeiroNome == "josé " or primeiroNome == "JOSÉ ":
    print(nome)
