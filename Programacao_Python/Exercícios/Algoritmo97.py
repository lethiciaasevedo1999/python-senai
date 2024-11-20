'''Entrar comum número e informarse ele é divisívelpor 10, por 5, por2 ou se não é
divisível por nenhum destes.'''

numero = int(input("Digite um número: "))

if numero % 10 == 0 or numero % 5 == 0 or numero % 2 == 0:
    print(f"O número {numero} é divisível por 10, por 5 ou 2")

else:
    print(f"O número {numero} não é divisível por nenhum destes")