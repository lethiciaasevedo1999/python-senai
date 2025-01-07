limite = int(input("Digite a quantia de números que deseja somar: "))

soma = 0
contador = 0

while contador <= limite:
    if contador % 2 > 0:
        print(contador)
    contador +=1