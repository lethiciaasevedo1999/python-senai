#Entrar com as notas da PR 1 e PR2 e imprimir a média final:
# truncada:
#arredondada:

from scipy.stats import trim_mean  
import math

pr1 = float(input("Digite a nota da PR1: "))
pr2 = float(input("Digite a nota da PR2: "))

media = (pr1 + pr2)/2
mediaTruncada = trim_mean((media - 0.5)+0.001)
mediaArredondada = math.ceil(media+ 0.001)

print(f"Média truncada: {mediaTruncada:.2f}\n"
      f"Média arredondada: {mediaArredondada}")