# Constantes --> Variáveis que não mudam o seu tipo em nenhuma hipotese
# Variáveis --> Variáveis que vão mudar de acordo com a necessidade 

# Vetores --> São arrays unidimensionais ou variáveis compostas de compartimentos 
# onde se podem armazenar vários valores em linha reta.
# Vetor: { 0 1 2 3 4 5 6 7 8 9} --> esse vetor possui 10 posições, pois começa em zero. 

#Matrizes --> São bidimensionais, trabalham com linhas e colunas

txt = "Jorge"

print(f"Na posição 0: {txt[0]}")
print(f"Na posição 1: {txt[1]}")
print(f"Na posição 2: {txt[2]}")
print(f"Na posição 3: {txt[3]}")
print(f"Na posição 4: {txt[4]}")

#Copiando o valor da posição da String
aux = []
aux.append(txt[0])
print(aux)

#Calculando o tamanho da minha variável 
con = len(txt)
print(con)

#Manipulando posições
print(txt[13]) # --> Quando sabemos exatamente o tamanho da variável
print(txt[-1]) # --> Ele vai identificar a última variável automaticamente 