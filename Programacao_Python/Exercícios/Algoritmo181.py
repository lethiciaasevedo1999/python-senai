#Criar um algoritmo que imprima todos os números de 1 a 100 e a soma deles

soma = 0 

for i in range(1, 101):
    soma = soma + i
    print(f" { i } , soma : {soma}")