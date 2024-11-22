'''Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
Entrar com o valor do produto e imprimir o valor da venda.'''

valorProduto = float(input("Digite o valor do produto: "))

if valorProduto < 20:
    print(f"Valor do produto: R$ {valorProduto}\n"
          f"Valor de venda: R$ {((45 * valorProduto)/100) + valorProduto:.2f}")
else:
    print(f"Valor do produto: R$ {valorProduto}\n"
          f"Valor de venda: R$ {((30 * valorProduto)/100) + valorProduto:.2f}")