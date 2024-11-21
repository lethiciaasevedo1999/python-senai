'''Entrar com a idade de uma pessoa e informar:
    - se é maior de idade
    - se é menor deidade
    - se é maior de 65 anos'''

idade = int("Digite sua idade: ")

if idade >= 18:
    print("Maior de idade")
elif idade < 18:
    print("Menor de idade")
elif idade > 65:
    print("Maior de 65 anos")