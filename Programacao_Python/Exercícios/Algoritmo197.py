'''Criar um algoritmo que leia um número que servirá para controlar os primeiros
números ímpares. Deverá ser impressa a soma desses números. Suponha que o número
será maior que zero:

Quantos: 5                                   Saída: 25
(1 2 5 7 9) - primeiros ímpares'''

numeros = int(input("Digite a quantia de números que deseja somar: "))

soma = 0
contador = 0
numero = 1


while contador < numeros:
    soma += numero
    contador += 1
    numero += 2

print(soma)

#Exercício ainda não resolvido por completo
