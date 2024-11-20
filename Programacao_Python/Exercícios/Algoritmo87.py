'''Criar um algoritmo que permita ao aluno responder qual a capital do Brasil. To-
das as possibilidades deverão ser pensadas.'''

resposta = input("Qual a capital do Brasil?: ")

if resposta == "Brasília" or resposta == "BRASÍLIA":
    print("Parabéns !!! Resposta CORRETA")
elif (resposta == "brasília" or resposta == "brazília" or resposta == "BRAZÍLIA" 
    or resposta == "brasilia" or resposta == "BRASILIA" or resposta == "brazilia" 
    or resposta == "BRAZILIA"):
    print("Resposta correta, mas atente-se a grafia correta: Brasília ou BRASÍLIA")
else:
    print("Resposta errada :/")