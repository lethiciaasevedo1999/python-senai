'''Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
mesmo número de pontos, criar um algoritmo que informe se uma equipe foi
classificada, de acordo com a seguinte especificação:
- ler os pontos obtidos por cada jogador da equipe;
- mostrar esses valores em ordem decrescente;
- se a soma dos pontos for maior do que 100, imprimir a média aritmética
entre eles; senão, imprimir a mensagem "Equipe desclassificada '''

pontos = []

for i in range (1, 4):
    pontos.append(int(input("Digite a pontuação: ")))

#Exibindo em ordem decrescente: 
pontos.sort()    
print(f"Pontuação: {pontos}")

#Soma
soma = sum(pontos)

#Operação:
if soma > 100:
    media = soma / 4
    print(f"Soma dos pontos: {soma}\n"
          f"Média aritmética: {media}")
else:
    print("Equipe DESCLASSIFICADA !")