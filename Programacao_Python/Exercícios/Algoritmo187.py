'''Criar um algorítmo que calcule e imprima o valor de b elevado a n. 
O valor de n deverá ser maior que 1 e inteiro e o valor de b maior ou igual 
a 2 e inteiro'''

b = int(input("Insira o valor de b: "))
n = int(input("Insira o valor de n: "))

if b > 2 and n > 1:
    calculo = b ** n
    print(f"b elevado a n é igual a : {calculo}")
else: 
   print("Valores inseridos são inválidos") 
    

