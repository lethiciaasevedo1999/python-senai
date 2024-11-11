'''Ler dois números reais e imprimir o quadrado da diferença do primeiro valor pelo
segundo e a diferença dos quadrados.'''

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

quadrado = numero1 ** 2 - numero2 ** 2
diferenca =  (numero1 - numero2) ** 2

print(f"Quadrado da diferença: {quadrado}\n"
      f"Diferença dos quadrados: {diferenca}")