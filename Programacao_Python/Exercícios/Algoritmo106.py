'''Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar
letra minúscula ou maiúscula).'''

nome = input("Digite o seu primeiro nome: ")
primeiraLetra = (nome[0])

if primeiraLetra == "A" or primeiraLetra == "a":
    print(nome)
