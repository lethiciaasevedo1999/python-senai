#16) Faça um programa que realize o cadastro de um usuário a partir de seu nome,
#idade, peso, altura que deverão ser informados pelo usuário e exiba a frase: 
#Seu nome é ______ e tem ___ caracteres, você tem ___ anos e nasceu no ano de ______. 
#Você mede _____cm, pesa ____ Kg e seu IMC é:____. 

#Não esqueça de manter uma boa interface com o usuário!! 

#*Fórmula do cálculo do IMC: IMC = Peso ÷ (Altura × Altura)

#Dados usuário
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso + (altura*altura)

print(f"Seu nome é {nome} e tem {len(nome)} caracteres, você tem {idade} anos "
      f"e nasceu no ano de {2024 - idade}. Você mede {altura}cm, pesa {peso}Kg "
      f"e seu IMC é: {imc}.")