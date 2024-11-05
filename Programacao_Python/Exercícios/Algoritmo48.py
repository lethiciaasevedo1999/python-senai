'''Antes de o racionamento de energia ser decretado, quase ninguém falava em

quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário. Sa-
bendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,

fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilo-
watts gasta por uma residência e calcule. Imprima:
- o valor em reais de cada quilowatt
- o valor em reais a ser pago
- o novo valor a ser pago por essa residência com um desconto de 10%.'''

salarioMinimo = float(input("Digite o valor do salaário mínimo: "))
quantiaQuilowatts = float(input("Digite a quantia de Quilowatts gasto em sua residência: "))
cemQuilowatts = salarioMinimo/7
umQuilowatts = salarioMinimo/100
valor = salarioMinimo/700
valoraPagar = valor * quantiaQuilowatts
desconto = valoraPagar * 0.10

print(f"Cada quilowatts custa R${umQuilowatts:.2f}\n"
      f"O valor em reais a ser pago é R${valoraPagar:.2f}\n"
      f"O novo valor a ser pago com desconto é R${valoraPagar - desconto:.2f}")



