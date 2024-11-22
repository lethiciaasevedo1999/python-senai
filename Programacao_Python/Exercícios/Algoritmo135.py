'''Criar um algoritmo que leia a idade de uma pessoa e informara sua classe eleitoral:
    - não-eleitor (abaixo de 16 anos)
    - eleitor obrigatório (entre 18 e 65 anos)
    - eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)'''

idade = int(input("Informe sua idade: "))

if idade < 16:
    print(f"Idade: {idade}\n"
           "Classe eleitoral: Não eleitor")
elif idade >= 18 and idade <= 65:
    print(f"Idade: {idade}\n"
           "Classe eleitoral: Eleitor obrigatório")
elif idade >= 16 and idade <= 18 or idade > 65:
    print(f"Idade: {idade}\n"
           "Classe eleitoral: Eleitor facultativo")