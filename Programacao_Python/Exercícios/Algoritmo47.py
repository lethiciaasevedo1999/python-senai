'''Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo:
123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser
impresso.''' 

numero = int(input("Digite um número de 3 dígitos: "))
palavra = (input("Digite uma palavra de 3 letras: "))

numeroInvertido = int(str(numero)[::-1])
palavraInvertida = palavra[::-1]

print(numeroInvertido)
print(palavraInvertida)


#Outra forma de fazer o exercício
numero2 = input("Digite um número de 3 dígitos: ")
numeroInvertido2 = int((numero2)[::-1])
print(numeroInvertido2)