#Entrar com a razão de uma PG e o valor do 1º termo. Calcular e imprimir o 5º termo da série: 

razao = int(input("Digite a razao: "))
termo = int(input("Digite o termo: "))

quinTermo = termo * razao ** 4

print(f"O 5º termo da P.G é: {quinTermo}")