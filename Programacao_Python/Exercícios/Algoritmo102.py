'''Entrar com um número e imprimir uma das mensagens: maior do que 20, igual a
20 ou menor do que 20.'''

numero = int(input("Digite um número: "))

if numero > 20:
    print("Número maior que 20")
elif numero == 20:
    print("Número igual a 20")
elif numero < 20:
    print("Número menor que 20")