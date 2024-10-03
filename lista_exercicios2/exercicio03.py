
#3)	Faça um programa que pede duas notas de um aluno. Em seguida ele deve 
# calcular a média do aluno e dar o seguinte resultado:
#•	Aprovado  Acima de 7
#•	Reprovado  Abaixo de 5
#•	Recuperação  Entre 5 e 7

print ("Olá, vamos calcular a média do aluno logo abaixo: ")

nota1 = float(input("Digite aqui a primeira nota de 0 a 10: "))
nota2 = float(input("Digite aqui a segunda nota de 0 a 10: "))

media = (nota1 + nota2) / 2

if media > 7:
    print("Parabéns, você foi APROVADO!!!")
elif media >= 5 and media <= 7:
    print("Você está de RECUPERAÇÃO, estude mais um pouco.")
else:
    print("Que pena, você foi REPROVADO :(")