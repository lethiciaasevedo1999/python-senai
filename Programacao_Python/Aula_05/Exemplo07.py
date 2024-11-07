#Desafio Escola do Tio Sam

nivel = float(input("Digite o valor da sua mensalidade: "))
dia = int(input("Digite o dia de hoje em número: "))

NivelI = 51.50
NivelII = 65.00
NivelIII = 80.00
NivelIV = 100.00


if nivel == NivelI and dia == 1: #NIVEL 1
    desconto = 15 * NivelI/100
    print("Você está no nível I")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelI - desconto:.2f}")
elif nivel == NivelI and dia <= 5 or dia == 5:
    desconto = 10 * NivelI/100
    print("Você está no nível I")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelI - desconto:.2f}")
elif nivel == NivelI and dia <= 10 or dia == 10:
    desconto = 3.89 * NivelI/100
    print("Você está no nível I")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelI - desconto:.2f}")
elif nivel == NivelII and dia == 1: # NIVEL 2
     desconto = 15 * NivelII/100
     print("Você está no nível II")
     print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelII - desconto:.2f}")
elif nivel == NivelII and dia <= 5 or dia == 5:
    desconto = 10 * NivelII/100
    print("Você está no nível II")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelII - desconto:.2f}")
elif nivel == NivelII and dia <= 10 or dia == 10:
    desconto = 3.89 * NivelII/100
    print("Você está no nível II")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelII - desconto:.2f}")
elif nivel == NivelIII and dia == 1: # NIVEL 3
    desconto = 15 * NivelIII/100
    print("Você está no nível III")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
elif nivel == NivelIII and dia <= 5 or dia == 5:
    desconto = 10 * NivelIII/100
    print("Você está no nível III")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
elif nivel == NivelIII and dia <= 10 or dia == 10:
    desconto = 3.89 * NivelIII/100
    print("Você está no nível III")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
elif nivel == NivelIV and dia == 1: # NIVEL 4
    desconto = 15 * NivelIV/100
    print("Você está no nível IV")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
elif nivel == NivelIV and dia <= 5 or dia == 5:
    desconto = 10 * NivelIV/100
    print("Você está no nível IV")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
elif nivel == NivelIV and dia <= 10 or dia == 10:
    desconto = 3.89 * NivelIV/100
    print("Você está no nível IV")
    print(f"O seu desconto vai ser de R${desconto:.2f} e o valor da sua mensalidade ficará R${NivelIII - desconto:.2f}")
else:
    print(f"Valor da mensalidade R$: {nivel} ")

