#8)	Faça um programa de um caixa eletrônico que, a partir do valor a ser sacado informado
#pelo usuário, o programa informe a menor quantidade de cédulas que o usuário irá 
#receber, informando-o quantas cédulas e de quais valores ele irá receber.
#Considerar apenas notas:
#R$200,00
#R$100,00
#R$50,00
#R$20,00
#R$10,00
#R$5,00
#R$2,00
#R$1,00

#Exemplo: R$ 858,00

#O programa irá informar:
#Cédulas de 200 reais: 4
#Cédulas de 50 reais: 1
#Cédulas de 5 reais: 1
#Cédulas de 2 reais: 1
#Cédulas de 1 real: 1

valor = int(input("Digite o valor que deseja receber: "))


if valor >= 200:
    quantiaNotas200 = valor // 200
    valor = valor % 200
    print(f"Notas de 200: {quantiaNotas200}")

if valor >= 100:
    quantiaNotas100 = valor // 100
    valor = valor % 100
    print(f"Notas de 100: {quantiaNotas100}")

if valor >= 50:
    quantiaNotas50 = valor // 50
    valor = valor % 50
    print(f"Notas de 50: {quantiaNotas50}")

if valor >= 20:
    quantiaNotas20 = valor // 20
    valor = valor % 20
    print(f"Notas de 20: {quantiaNotas20}")

if valor >= 10:
    quantiaNotas10 = valor // 10
    valor = valor % 10
    print(f"Notas de 10: {quantiaNotas10}")

if valor >= 5:
    quantiaNotas5 = valor // 5
    valor = valor % 5
    print(f"Notas de 5: {quantiaNotas5}")



















