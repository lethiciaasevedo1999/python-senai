#Entrar com dois numeros inteiros e imprimir a seguinte saída: 

''' dividendo:
    divisor:
    quociente:
    resto'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

dividendo = numero1
divisor = numero2
quociente = numero1 / numero2
resto = numero1 % numero2


print(f'''
      Dividendo: {dividendo}
      Divisor: {divisor}
      Quociente: {quociente}
      Resto: {resto}
      ''')


