#4)	Uma ótica quer fazer um desconto diferenciado com base na idade do usuário
#em um modelo de óculos que custa R$200,00. O desconto será igual a idade do usuário, 
#porém o desconto mínimo será 10% e o desconto máximo será de 80%.
# Faça um programa que pergunte a idade do usuário e então mostre o valor final 
#do óculos e o desconto adquirido.

idadeUsuario = int(input("Insira sua idade por favor: "))

valorInicial = 200.00
desconto = valorInicial *(idadeUsuario/100)
valorFinal = valorInicial - desconto

if idadeUsuario < 10:
    desconto = valorInicial * (10/100)
elif idadeUsuario > 80:
    desconto = valorInicial * (80/100)

print(f"O valor final do seu óculos será de {valorInicial - desconto}R$, equivalente" 
      f" a {idadeUsuario}% de desconto.")





