'''Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para cal-
cular seu rendimento, ela deverá fornecer o valor constante da aplicação mensal, a

taxa e o número de meses. Sabendo-se que a fórmula usada para este cálculo é:
fl ' + 1 valor acumulado = P * ' . - i = taxa

P = aplicação mensal
n= número de meses'''

aplicacaoMensal = float(input("Digite o valor da sua aplicação: "))
taxa = float(input("Digite o valor da taxa: "))
meses = int(input("Digite o número de meses: "))

valorAcumulado = aplicacaoMensal * (((1 + taxa) ** meses) - 1) / taxa

print(f"O valor acumulado é: {valorAcumulado}")

