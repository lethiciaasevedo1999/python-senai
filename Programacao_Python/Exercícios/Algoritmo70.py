'''Todo restaurante embora por lei não possa obrigar o cliente a pagar, cobra 10%
para o garçom. Fazer um algoritmo que leia o valor gasto com despesas realiza-
das em um restaurante e imprima o valor total com a gorjeta.'''

valorGasto = float(input("Digite o valor gasto no restaurante: "))
gorjeta = valorGasto * (10/100)

print(f"O valor total com a gorjeta é: {valorGasto + gorjeta:.2f}")