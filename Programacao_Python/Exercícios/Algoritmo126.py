'''Ler um número e imprimir se ele é iguala 5, a 200, a 400, se está no intervalo en-
tre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.'''

numero = int(input("Digite um número: "))

if numero == 5 :
    print("Número é igual a 5")
elif  numero == 200:
    print("Número é igual a 200")
elif numero == 400:
    print("Número é igua a 400")
elif numero >= 500 and numero <= 1000:
    print("O número está no intervalo de 500 a 1000")
else:
    print("O número não se enquadra em nenhum dos escopos anteriores")