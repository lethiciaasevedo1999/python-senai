'''Criar um algoritmo que efetue o cálculo do salário líquido de um professor. Os da-
dos fornecidos serão: valor da hora aula, número de aulas dadas no mês e per-
centual de desconto do INSS.'''

horaAula = float(input("Digite o valor da hora aula: "))
aulasMes = int(input("Digite o número de aulas dadas no mês: "))
descontoInss = float(input("Qual o valor do percentural de INSS descontado?: "))
salarioBase = aulasMes * horaAula
totalDesconto = (descontoInss/ 100) * salarioBase
salarioLiquido = salarioBase - totalDesconto

print(f"Valor líquido a receber: {salarioLiquido}")