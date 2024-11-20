'''Criar um algoritmo que, dado um número de conta corrente com três dígitos, re-
torne o seu dígito verificador, o qual é calculado da seguinte maneira:

Exemplo: número da conta: 235
Somar o número da conta com o seu inverso: 235+ 532 = 767
multiplicar cada dígito pela sua ordem posicional e somar estes resultados: 767

7 6 7
Xl X2 X3
7 + 12 + 21 =40

o último dígito desse resultado é o dígito verificador da conta (40 -> 0).'''

numeroConta = int(input("Digite os 3 primeiros dígitos da sua conta: "))
numeroInverso = int(str(numeroConta)[::-1])
soma = numeroConta + numeroInverso
soma_str = str(soma) #convertendo o resultado de soma para string
resultado = (int(soma_str[0]) *1) + (int(soma_str[1]) * 2) + (int(soma_str[2]) * 3)
resultado_str = str(resultado)
digito_verificador = int(resultado_str[-1]) 

print(f"Dígito verificador : {digito_verificador}")

