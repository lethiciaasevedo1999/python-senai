#Entrar com a razão de uma PA e o valor do 1º termo. Calcular e imprimir o 10º termo da série

termo = int(input("Digite o termo: "))
razao = int(input("Digite a razao: "))

decTermo = termo + 9 * razao

print(f"O 10º termo desta P.A é: {decTermo}")