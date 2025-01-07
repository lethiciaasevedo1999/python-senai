'''Criar um algoritmo que leia um número e imprima a soma dos números múltiplos
de 5 no intervalo aberto entre 1 e numero. Suponha que numero será maior que zero:

Limite superior: 15                         Saída: 15
(5 10) - múltiplo de 5                                                         '''

limite = int(input("Insira o número limite: "))

soma = 0

for i in range (1, limite + 1):
    if i % 5 == 0:
        soma += i

print(soma)