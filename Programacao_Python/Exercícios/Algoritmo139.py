'''Sabendo que somente os municípios que possuem mais de 20.000 eleitores ap-
tos têm segundo turno nas eleições para prefeito caso o primeiro colocado não
tenha mais do que 50% dos votos, fazer um algoritmo que leia o nome do municí-
pio, a quantidade de eleitores aptos, o número de votos do candidato mais vota-
do e informar se ele terá ou não segundo turno em sua eleição municipal.'''

nomeMunicipio = input("Digite o nome do município: ")
quantidadeEleitores = float(input("Insira o número de eleitores: "))
numeroVotos = float(input("Insira o número de votos: "))

porcento50 = numeroVotos / 2

if numeroVotos > porcento50 and quantidadeEleitores > 20.000:
    print("*"*40)
    print("      RESULTADO ELEIÇÕES      ")
    print("*"*40)
    print(f"Nome do município: {nomeMunicipio}\n"
          f"Quantia de eleitores aptos: {quantidadeEleitores}\n"
          f"Número de votos: {numeroVotos}\n"
          f"Situação: terá segundo turno")
else:
    print("*"*40)
    print("         RESULTADO ELEIÇÕES      ")
    print("*"*40)
    print(f"Nome do município: {nomeMunicipio}\n"
          f"Quantia de eleitores aptos: {quantidadeEleitores}\n"
          f"Número de votos: {numeroVotos}\n"
          f"Situação: não terá segundo turno")