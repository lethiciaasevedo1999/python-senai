#17) Um fabricante de tintas quer montar um programa que auxilie o 
#comprador a saber quantas latas de tinta ele precisará para pintar sua parede. 
#Monte um programa em python que execute esta função a partir dos dados 
#informados pelo usuário (largura e altura), sabendo que cada lata de tinta 
#cobre 3m² de parede. 

#Não esqueça de manter uma boa interface com o usuário!!

print("Olá, vamos calcular quantas latas de tinta você vai precisar :)")

largura = float(input("Qual é a largura da sua parede? : "))
altura = float(input("Qual é a altura da sua parede ? : "))

metroQuadrado = largura * altura
latasNecessarias = round(metroQuadrado / 3) + 1

print(f"Você vai precisar de {latasNecessarias:.2f} latas de tinta para pintar sua parede.")