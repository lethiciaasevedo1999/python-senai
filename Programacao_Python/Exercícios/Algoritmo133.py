'''Segundo uma tabela medica o peso ideal esta relacionado com a altura e o sexo

Fazer um algoritmo que receba a altura e o sexo de uma pessoa, calcular e imprimir 
o seu peso ideal utilizando as seguintes formulas

para homens: (72.7 * H) -58
para mulheres (62 1 * H) -44 7'''

altura = float(input("Digite sua altura: "))
sexo = input("Digite F para feminino e M para masculino: ")

if sexo == "f" or sexo == "F":
    pesoIdeal = (62 * altura) - 44.7
    print(f"Peso ideal: {pesoIdeal}")
elif sexo == "m" or sexo == "M":
    pesoIdeal = (72.7 * altura) - 58
    print(f"Peso ideal: {pesoIdeal}")

