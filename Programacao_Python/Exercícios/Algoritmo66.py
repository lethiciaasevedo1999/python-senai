'''Efetuar o cálculo da quantidade de litros de combustível gastos em uma viagem,
sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos o tempo
gasto na viagem e a velocidade média.
Utilizar as seguintes fórmulas: distância = tempo x velocidade.
litros usados = distância / 12.
O algoritmo deverá apresentar os valores da velocidade média, tempo gasto
na viagem, distância percorrida e a quantidade de litros utilizados na viagem.'''

tempo = float(input("Digite o tempo gasto na viagem: "))
velocidadeMedia = float(input("Digite a velocidade média: "))
distancia = tempo * velocidadeMedia
litros = distancia / 12

print(f"Velocidade média: {velocidadeMedia:.2f} K/H\n"
      f"Tempo gasto: {tempo:.2f} hrs\n"
      f"Distância percorrida: {distancia:.2f} KM\n"
      f"Litros utilizados na viagem: {litros:.2f} litros\n")