#Imprimir nome e CPF de 5 pessoas 

i = 1

while(i <= 5):
    nomeCPF = input("Digite o seu nome e o CPF: ")
    print(nomeCPF)
    
    i+=1 
    
#Outro modo    
while(i <= 5):
    nome = input("Digite o seu nome: ")
    cpf = int(input("Digite o seu CPF: "))
    print(f'{nome} - {cpf}')    
    
    i+=1