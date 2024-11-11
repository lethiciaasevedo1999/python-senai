'''Dado um polígono convexo de n lados, podemos calcular o número de diagonais
diferentes (nd) desse polígono pela fórmula : nd = n (n —3)! 2. Fazer um algorit-
mo que leia quantos lados tem o polígono, calcule e escreva o número de diago-
nais diferentes (nd) do mesmo.'''

lados = int(input("Digite o número de lados do polígono: "))
numeroDiagonais = lados * (lados - 3) / 2

print(f"O número de diagonais diferentes do polígono é: {numeroDiagonais}")