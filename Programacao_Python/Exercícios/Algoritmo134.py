'''A confederação brasileira de natação irá promover eliminatórias para o próximo
mundial Fazer um algoritmo que receba a idade de um nadador e imprimir a sua
categoria segundo a tabela a seguir:

Categoria Idade
InfantilA 5-7anos
Infantil B 8— 10 anos
JuvenilA 11 - 13 anos
Juvenil 14— 17 anos
Sênior maiores de 18 anos'''

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 7:
    print(f"Idade: {idade} anos\n"
          "Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print(f"Idade: {idade} anos\n"
          "Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print(f"Idade: {idade} anos\n"
          "Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print(f"Idade: {idade} anos\n"
          "Categoria: Infantil B")
elif idade >= 18:
    print(f"Idade: {idade} anos\n"
          "Categoria: Sênior")