#Calculadora com função 

#Soma
def soma (a, b):
    resultado = a + b
    return resultado

valor01 = int(input("Digite um número: "))
valor02 = int(input("Digite outro número: "))
totalSoma = soma(valor01,valor02)
print(f"Resultado da soma: {totalSoma} ")

#Subtração
def subtracao (a, b):
    resultado = a - b
    return resultado

valor01 = int(input("Digite um número: "))
valor02 = int(input("Digite outro número: "))
totalSubtracao = subtracao(valor01,valor02)
print(f"Resultado da soma: {totalSubtracao} ")

#Multiplicação
def multiplicacao (a, b):
    resultado = a * b
    return resultado

valor01 = int(input("Digite um número: "))
valor02 = int(input("Digite outro número: "))
totalMultiplicacao = multiplicacao(valor01,valor02)
print(f"Resultado da soma: {totalMultiplicacao} ")


#Divisão
def divisao (a, b):
    resultado = a + b
    return resultado

valor01 = int(input("Digite um número: "))
valor02 = int(input("Digite outro número: "))
totalDivisao = divisao(valor01,valor02)
print(f"Resultado da soma: {totalDivisao} ")

