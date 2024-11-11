'''Para vários tributos, a base de cálculo é o salário mínimo. Fazer um algoritmo que
leia o valor do salário mínimo e o valor do salário de uma pessoa. Calcular e impri -
mir quantos salários mínimos ela ganha.'''

salarioMinimo = float(input("Digite o valor do salário mínimo: "))
salarioPessoa = float(input("Digite o valor do seu salário: "))

salarios = salarioPessoa / salarioMinimo

print(f"Você recebe: {salarios:.2f} salários mínimos")