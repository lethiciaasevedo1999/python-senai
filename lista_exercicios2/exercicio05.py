#5)	Uma empresa pretende fazer um reajuste salarial para os funcionários 
# e precisa da sua ajuda para criar um programa. 
# Ficou definido os seguintes reajustes:
#•	Salário Abaixo de R$1.500,00  Aumento de 25%
#•	Salário Entre de R$1.500,00 e R$1.999,99 --> Aumento de 20%
#•	Salário Entre de R$2.000,00 e R$2.999,99 --> Aumento de 15%
#•	Salário Entre de R$3.000,00 e R$4.999,99 --> Aumento de 10%
#•	Salário Acima de R$5.000,00 --> Aumento de 5%

#Faça um programa que pergunte ao usuário qual seu Salário Atual e mostre ao usuário:
#1.	O salário atual;
#2.	A porcentagem do reajuste;
#3.	O aumento em R$;
#4.	O salário final após o reajuste.


salarioAtual = float(input("Digite o seu salário atual: "))


if salarioAtual < 1500:
    ajuste = salarioAtual * (25/100)
    print(f"Salário atual: {salarioAtual} \n"
          f"Porcentagem do reajuste: 25% \n"
          f"Valor em R$: {round(ajuste)}\n"
          f"Salário final: {round(salarioAtual + ajuste)}R$" )
elif salarioAtual >= 1500.00 and salarioAtual <= 1999.99:
    ajuste = salarioAtual * (20/100)
    print(f"Salário atual: {salarioAtual} \n"
          f"Porcentagem do reajuste: 20% \n"
          f"Valor em R$: {round(ajuste)}\n"
          f"Salário final: {round(salarioAtual + ajuste)}R$" )
elif salarioAtual >= 2000.00 and salarioAtual <= 2999.99:
    ajuste = salarioAtual * (15/100)
    print(f"Salário atual: {salarioAtual} \n"
          f"Porcentagem do reajuste: 15% \n"
          f"Valor em R$: {round(ajuste)}\n"
          f"Salário final: {round(salarioAtual + ajuste)}R$" )
    
elif salarioAtual >= 3000.00 and salarioAtual <= 4999.99:
    ajuste = salarioAtual * (10/100)
    print(f"Salário atual: {salarioAtual} \n"
          f"Porcentagem do reajuste: 10% \n"
          f"Valor em R$: {round(ajuste)}\n"
          f"Salário final: {round(salarioAtual + ajuste)}R$" )
    
else:
    ajuste = salarioAtual * (5/100)
    print(f"Salário atual: {salarioAtual} \n"
          f"Porcentagem do reajuste: 5% \n"
          f"Valor em R$: {round(ajuste)}\n"
          f"Salário final: {round(salarioAtual + ajuste)}R$" )
     