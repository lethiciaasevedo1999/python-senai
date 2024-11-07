#Condicionais com cálculos , média 

nota01 = float(input("Digite a note: "))
nota02 = float(input("Digite a note: "))
nota03 = float(input("Digite a note: "))
nota04 = float(input("Digite a note: "))

media = (nota01+nota02+nota03+nota04)/4

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")