'''Fazer um algoritmo que possa converter uma determinada quantia dada em reais
para uma das seguintes moedas:
    - f- franco suíço
    - l - libra esterlina
    - d - dólar
    - m - marco alemão'''

print("*"*20)
print("CONVERSOR DE MOEDAS")
print("*"*20)
print("      Moedas     \n"
      "F - Franco Suíço\n"
      "L - Libra\n"
      "D - Dólar\n"
      "M - Marco Alemão\n")
opcao = input("Selecione a opção desejada: ")
valor = float(input("Digite o valor que deseja converter: "))

if opcao == "f" or opcao == "F":
    valorCorrigido = valor * 6.56
    print(f"Real brasileiro: R$ {valor}\n"
          f"Franco suíço: CHF {valorCorrigido}")
elif opcao == "l" or opcao == "L":
    valorCorrigido = valor * 7.32
    print(f"Real brasileiro: R$ {valor}\n"
          f"Libra: £ {valorCorrigido}")
elif opcao == "d" or opcao == "D":
    valorCorrigido = valor * 5.82
    print(f"Real brasileiro: R$ {valor}\n"
          f"Dólar: $ {valorCorrigido}")
elif opcao == "m" or opcao == "M":
    valorCorrigido = valor * 3.12
    print(f"Real brasileiro: R$ {valor}\n"
          f"Marco alemão: DEM {valorCorrigido}")