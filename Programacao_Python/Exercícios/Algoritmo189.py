'''Criar um algoritmo que imprima a tabela de conversão de graus Celsius-Fahrenheit
para o intervalo desejado pelo usuário. O algoritmo deve solicitar ao usuário o limite 
superior, o limite inferior do intervalo e o decremento.
Fórmula de conversão: C =5 (F - 32) / 9'''

limiteInferior = int(input("Digite o limite inferior: "))
limiteSuperior = int(input("Digite o limite superior: "))
incremento = int(input("Digite o valor do incremento: "))


print("\nTabela de Conversão Celsius-Fahrenheit")
print("-------------------------------------")
print("Celsius\t\tFahrenheit")


for celsius in range(limiteInferior, limiteSuperior + 1, incremento):
    fahrenheit = (celsius * 9 / 5) + 32  
    print(f"{celsius}\t\t{fahrenheit:.2f}")