'''Criar um algoritmo que imprima uma tabela de conversão de polegadas para cen-
tímetros. Deseja-se que na tabela conste valores desde 1 polegada até 20 polega-
das inteiras.'''

contador = 0

for i in range(1, 21):
    i = i / 2.5
    contador = contador + 1
    print(f"{contador} cm -->  {i} polegadas")