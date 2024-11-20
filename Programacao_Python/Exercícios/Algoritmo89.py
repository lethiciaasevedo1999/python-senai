'''Escrever um algoritmo que leia um peso na Terra e o numero de um plane-
ta e imprima o valor do seu peso nesteplaneta A relação de planetas é

dada a seguir Juntamente com o valor das gravidades relativas a Terra
# gravidade relativa Planeta
1 0,37 Mercúrio
2 09 88 Vênus
3 0,38 Marte
4 2,64 Júpiter
5 1 9 15 Saturno
6 1,17 Urano 77

Para calcular o peso no planeta use a fórmula:
Pplaneta. Pterra. gravidade'''

print(''' 
      *************************\n
               PLANETAS
      *************************\n
      1 - MERCÚRIO\n
      2 - VÊNUS\n
      3 - MARTE\n
      4 - JÚPTER\n
      5 - SATURNO\n
      6 - URANO

''')

planetaEscolhido = int(input("Digite a opção escolhida: "))

pesoTerra = float(input("Digite o seu peso: "))

if planetaEscolhido == 1:
    peso = (pesoTerra/10) *0.37
    print(f"Peso em Mercúrio: {peso}")
elif planetaEscolhido == 2:
    peso = (pesoTerra/10) *0.88
    print(f"Peso em Vênus: {peso}")
elif planetaEscolhido == 3:
    peso = (pesoTerra/10) *0.38
    print(f"Peso em Marte: {peso}")
elif planetaEscolhido == 4:
    peso = (pesoTerra/10) *2.64
    print(f"Peso em Júpter: {peso}")
elif planetaEscolhido == 5:
    peso = (pesoTerra/10) *1.15
    print(f"Peso em Saturno: {peso}")
elif planetaEscolhido == 6:
    peso = (pesoTerra/10) *1.17
    print(f"Peso em Urano: {peso}")