#15) Uma professora gostaria um programa para auxiliá-la a montar a 
#média final de seus alunos. Sabendo que são 2 notas por semestre, 
#monte um programa que através das notas informadas pelo usuário mostre 
#a sua média final. Não esqueça de manter uma boa interface com o usuário!!

#Primeiro semestre
print("Digite as notas do primeiro semestre por favor: ")
sem1Nota1 = float(input("Digite a primeira nota: "))
sem1Nota2 = float(input("Digite a segunda nota: "))

#Segundo semestre
print("Digite as notas do segundo semestre por favor: ")
sem2Nota1 = float(input("Digite a primeira nota: "))
sem2Nota2 = float(input("Digite a segunda nota: "))

mediaFinal = (sem1Nota1 + sem1Nota2 + sem2Nota1 + sem2Nota2) / 4

print(f"A média final do seu aluno é: {mediaFinal}")