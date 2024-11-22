'''Entrar com um verbo no infinitivo e imprimir uma das mensagens:
    - verbo não está no infinitivo
    - verbo da 1a conjugação
    - verbo da 2a conjugação
    - verbo da 3 conjugação'''

verbo = input("Digite o verbo: ")
final = (verbo[-2:])

if final == "ar":
    print(f"Verbo: {verbo}\n"
          f"Classificação: 1a conjugação ")
elif final == "er":
    print(f"Verbo: {verbo}\n"
          f"Classificação: 2a conjugação ")
elif final == "ir":
    print(f"Verbo: {verbo}\n"
          f"Classificação: 3a conjugação ")
else:
    print(f"Verbo: {verbo}\n"
          "Classificação: Outras categorias")