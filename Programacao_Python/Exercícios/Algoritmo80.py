'''
Criar um algoritmo que leia a quantidade de fitas que uma locadora de vídeo pos-
sui e o valor que ela cobra por cada aluguel, mostrando as informações pedidas a
seguir:

- Sabendo que um terço das fitas são alugadas por mês, exiba o
faturamento anual da locadora;
- Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o
valor do aluguel. Sabendo que um décimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês;
- Sabendo ainda que 2% de fitas se estragam ao longo do ano, e um décimo
do total é comprado para reposição, exiba a quantidade de fitas que a locadora
terá no final do ano.'''

quantiaFitas = int(input("Digite o valor total de fitas que a locadora possui: "))
valorAluguel = float(input("Digite o valor do aluguel por cada fita: "))

alugueisMes = quantiaFitas / 3
faturamentoAnual =  ((quantiaFitas / 3 ) * 12) * valorAluguel
multaMes = ((alugueisMes / 10) * valorAluguel)
multaMes2 = multaMes + (multaMes * 10/100)
quantiaFinalAno = (quantiaFitas - (quantiaFitas * 2/100)) + (quantiaFitas / 10) 

print(f"Faturamento anual : R${faturamentoAnual}\n"
      f"Valor ganho com multas por mês: R${multaMes2:.2f}\n"
      f"Quantia de fitas no final do ano: R${quantiaFinalAno}")

print(((alugueisMes / 10) * valorAluguel))
