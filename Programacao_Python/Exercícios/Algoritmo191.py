'''Criar um algoritmo que leia um número que será o limite superiorde um intervalo o 
incremento. Imprimir todos os números naturais no intervalo de 0 até esse número.
Suponha que os dois números lidos são maiores do que zero, Exemplo: 

Limite superior: 20
Incremento: 5                                 Saída: 0 5 10 15 20'''

limite = int(input("Digite o número limite: "))
incremento = int(input("Digite o incremento: "))

i = 0
 
while i <= limite:
    print(i)
    i += incremento
      