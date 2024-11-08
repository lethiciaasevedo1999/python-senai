'''Entrar com valores para xnum1,xnum2 e xnum3 e imprimir o valor de x, sabendo-se que:  '''
# X = xnum1 + xnum2(xnum3 + xnum1) + 2 (xnum1 + xnum2) + log64,2
    
import math
    
xnum1 = int(input("Digite o primeiro número:  "))
xnum2 = int(input("Digite o primeiro número:  "))
xnum3 = int(input("Digite o primeiro número:  "))

x = xnum1 + xnum2 / (xnum3 + xnum1) + 2 * (xnum1 + xnum2) + math.log(64.) / math.log(2.)

print(f"X = {x}")