'''Entrar com um nome e imprimir:
    Todo o nome:
    Primeiro caractere: 
    Último caractere: 
    Do primeiro até o terceiro: 
    Quarto caractere: 
    Todos menos o primeiro: 
    Os dois últimos: 
'''

nome = input("Digite um nome: ")

print(f"Nome: {nome}\n"
      f"Último caractere: {nome[-1]}\n"
      f"Do primeiro até o terceiro: {nome[0:3]}\n"
      f"Quarto caractere: {nome[3]}\n"
      f"Todos menos o primeiro: {nome[1:]}\n"
      f"Os dois últimos: {nome[-2:]}")

