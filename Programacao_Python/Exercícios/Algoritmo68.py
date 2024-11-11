'''Ler dois valores para as variáveis A e B, efetuar a troca dos valores de forma que a

variávelA passe a ter o valor da variável B e que a variável B passe a ter o valor da va-
riável A. Apresentar os valores trocados.'''

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

a , b = b, a

print(f"Valor de A : {a}\n"
      f"Valor de B : {b}")