#Trabalhando com conficionais IF e ELSE

idade = int(input("Digite a idade da candidata: " ))
altura = float(input("Digite a altura da candidata: " ))


idadeEsperada = 15
alturaEsperada = 1.70

if idade == idadeEsperada and altura == alturaEsperada:
    print("-----------Candidata aprovada-----------")
else:
    print("-----------Candidata reprovada-----------")