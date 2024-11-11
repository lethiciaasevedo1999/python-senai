'''Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas
vendas oferecendo desconto. Faça um algoritmo que possa entrar com o valor de
um produto e imprima o novo valor tendo em vista que o desconto foi de 9%.'''

valorProduto = float(input("Digite o valor do seu produto: "))
desconto = valorProduto * (9 / 100)

print(f"O valor do seu produto com desconto é R${valorProduto - desconto:.2f}")