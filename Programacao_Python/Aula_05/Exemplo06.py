

idade = int(input("Digite a idade da candidata: " ))
altura = float(input("Digite a altura da candidata: " ))


idadeEsperada = 15
alturaEsperada = 1.70

# de 0 a 11 anos = Infantil
# de 12 a 17 anos = teen
# de 18 a 24 anos = jovem
# de 25 a 50 anos = adulto

if idade >= 0 and idade <= 11:
    print("----------Candidata aprovada----------")
    print("----------Categoria infantil----------")
elif idade >= 12 and idade <= 17 and alturaEsperada:
    print("----------Candidata aprovada----------")
    print("----------Categoria Teen----------")
elif idade >= 18 and idade <= 24 and alturaEsperada:
    print("----------Candidata aprovada----------")
    print("----------Categoria Jovem----------")
elif idade >= 25 and idade <= 50 and alturaEsperada:
    print("----------Candidata aprovada----------")
    print("----------Categoria adulto----------")
else:
    print("----------Candidata reprovada----------")