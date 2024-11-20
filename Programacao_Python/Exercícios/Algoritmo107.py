#Entrar com o nome de uma pessoa e so imprimi-lo se o prenome for JOSE

nome = input("Digite o seu nome: ")
primeiroNome = (nome[0:4])


if primeiroNome == "José " or primeiroNome == "josé " or primeiroNome == "JOSÉ ":
    print(nome)
