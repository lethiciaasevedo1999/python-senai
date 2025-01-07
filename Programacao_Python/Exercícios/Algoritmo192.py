'''Criar um algoritmo que leia um número que será o limite superior de um intervalor
e imprimir todos os números ímpares menores do que esse número. Exemplo: 

Limite superior : 15                      Saída: 1 2 5 7 9 11 13'''

limite = int(input("Digite o número limite: "))

for i in range (0, limite + 1):
    if i % 2 > 0:
        print(i)
        i += 1
