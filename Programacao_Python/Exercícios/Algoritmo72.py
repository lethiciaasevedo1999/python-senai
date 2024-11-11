'''Criar um algoritmo que leia o valor de um depósito e o valor da taxa de ju-
ros. Calcular e imprimir o valor do rendimento e o valor total depois do ren-
dimento.'''

valorDeposito = float(input("Digite o valor do seu depósito: "))
taxaJuros = float (input("Digite a taxa de juros: "))
valor = valorDeposito * taxaJuros/ 100
valorTotal = valorDeposito + valor

print(f"O valor final do seu redimento será de: {valorTotal}")