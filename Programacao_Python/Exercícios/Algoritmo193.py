'''Criar um algoritmo que leia um número que servirá para controlar os números pares
que serão impressos a partir de 2. Exemplo: 

Quantos: 4              Saída: 2 4 6 8'''

limite = int(input("Digite o número limite: "))

for i in range (0, limite + 1):
    if i % 2 == 0:
        print(i)
        i += 1
