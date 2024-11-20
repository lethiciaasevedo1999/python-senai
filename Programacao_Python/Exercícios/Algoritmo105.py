'''Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
    - carioca
    - paulista
    -mineiro
    -outros estados'''

estado = input("Digite a sigla do seu estado: ")

if estado == "SP" or estado == "sp":
    print("Você é paulista")
elif estado == "RJ" or estado == "rj":
    print("Você é carioca")
elif estado == "MG" or estado == "mg":
    print("Você é mineiro")
else: 
    print("Você é de outros estados.")