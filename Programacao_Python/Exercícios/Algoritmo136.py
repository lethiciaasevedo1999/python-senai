'''Depois da liberação do governo para as mensalidades dos planos de saúde, as
pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito
caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um
algoritmo que entre com o nome e a idade de uma pessoa e imprimir o nome e o
valor que ela deverá pagar.
    - ate l0 anos -R$ 30 00
    - acima de 10 até 29 anos - R$ 60,00
    - acima de 29 até 45 anos - R$ 120,00
    - acima de 45 até 59 anos - R$ 150,00
    - acima de 59 até 65 anos - R$ 250,00
    - maior que 65 anos - R$ 400,00'''

nome = input("Informe seu nome completo: ")
idade = int(input("Informe sua idade: "))

if idade <= 10:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 30,00")
elif idade > 10 and idade <= 29:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 60,00")
elif idade > 29 and idade <=45:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 120,00")
elif idade > 45 and idade <= 59:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 150,00")
elif idade > 59 and idade <= 65:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 250,00")
elif idade > 65:
    print("*"*30)
    print("          ORÇAMENTO    ")
    print("*"*30)
    print(f"Nome: {nome}\n"
          "Valor a pagar: R$ 400,00")