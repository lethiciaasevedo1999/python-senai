'''A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários es -
tatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
bruto Fazer um algoritmo que permita entrar com o salário bruto e o valor da
prestação e informar se o empréstimo pode ou não ser concedido.'''

salarioBruto = float(input("Digite o valor do seu salário bruto: "))
valorPrestacao = float(input("Digite o valor da prestação: "))

if valorPrestacao <= 0.3 * salarioBruto:
    print("Empréstimo concedido")
else:
    print("Empréstimo negado.")