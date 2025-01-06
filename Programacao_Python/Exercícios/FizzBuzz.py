# Teste FizzBuzz 
'''Escreva um programa que imprima os números de 1 a 100. Mas para múltiplos 
de três imprima "Fizz" em vez do número e para os múltiplos de cinco imprima 
"Buzz". Para números que são múltiplos de três e cinco, imprima "FizzBuzz"'''

n = int(input("Digite a quantia: "))

for i in range (1, n + 1):
  
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 5 > 0:
        print("Fizz")
    elif i % 5 == 0 and i % 3 > 0:
        print("Buzz")
    else :
        print ( i)