'''Efetuar o cálculo do valor de uma prestação em atraso, utilizando a fórmula:
prestação = valor + (valor*(taxa/100)*tempo).'''

valorPrestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa: "))
tempo = int(input("Digite o número de meses de atraso: "))

prestacao = valorPrestacao + (valorPrestacao*(taxa/100)*tempo)

print(f"O valor da prestação em atraso é: {prestacao}")