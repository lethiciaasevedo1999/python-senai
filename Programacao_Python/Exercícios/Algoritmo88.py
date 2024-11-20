# Algorítmo Calculadora

print("*****************************")
print("        *CALCULADORA*        ")
print("*****************************")

print('''Selecione a opção desejada:\n
      1 - ADIÇÃO\n
      2 - SUBTRAÇÃO\n
      3 - MULTIPLICAÇÃO\n
      4 - DIVISÃO ''')

opcao = int(input("Digite a opção: "))

num1 = float(input("Digite o número: "))
num2 = float(input("Digite o número: "))

if opcao == 1: #Adição
    operacao = num1 + num2
    print(f"Resultado: {operacao}")
elif opcao == 2: #Subtração
    operacao = num1 - num2
    print(f"Resultado: {operacao}")
elif opcao == 3: #Multiplicação
    operacao = num1 * num2
    print(f"Resultado: {operacao}")
elif opcao == 4: #Divisão
    operacao = num1 / num2
    print(f"Resultado: {operacao}")
