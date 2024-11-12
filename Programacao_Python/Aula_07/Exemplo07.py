

soma = 0

#Enquanto for verdadeiro oque eu coloquei dentro do loop
while(True):
    num = int(input("Digite um número: "))
    if (num < 0):
        break
    
    soma = soma + num
    
print(f"A soma dos números é: {soma}")