'''Entrar com o salário de uma pessoa e imprimir o desconto do INSS segundo a ta-
bela a seguir:

menor ou igual a R$ 600,00 isento
maior que R$ 600,00 e menor ou igual a R$ 1200,00 20%
maior que R$ 1200,00 e menor ou igual a R$2000,00 25%
maior que R$ 2000,00 30%'''

salario = float(input("Digite o valor do seu salário: "))

if salario <= 600:
    print(f"Salário: R${salario}\n"
          f"Desconto INSS: ISENTO.")
elif salario > 600 and salario <= 1200:
    print(f"Salário: R${salario}\n"
          f"Desconto INSS: {((20 * salario) / 100):.2f}")
elif salario > 1200 and salario <= 2000:
    print(f"Salário: R${salario}\n"
          f"Desconto INSS: {((25 * salario) / 100):.2f}")
elif salario > 2000:
    print(f"Salário: R${salario}\n"
          f"Desconto INSS: {((30 * salario) / 100):.2f}")