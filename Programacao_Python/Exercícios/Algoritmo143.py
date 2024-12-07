'''Criar um algoritmo que verifique a(s) letra(s) central(is) de uma palavra. Se o nu-
mero de caracteres for ímpar, ele verifica se a letra central é uma vogal; caso con-
trario verifica se e um dos digrafos rr ou ss (só precisa, testar letras minusculas)'''

palavra = input("Digite uma palavra: ")
totalPalavra = len(palavra)


centro = totalPalavra // 2

if totalPalavra % 2 > 0:  
    letra_central = palavra[centro]  
    if letra_central in "aeiou":
        print(f"A letra central é uma vogal: {letra_central}")
    else:
        print(f"A letra central não é uma vogal: {letra_central}")
else: 
    letras_centrais = palavra[centro - 1: centro + 1]  
    if letras_centrais in ["rr", "ss"]:  
        print(f"As letras centrais são um dígrafo: {letras_centrais}")
    else:
        print(f"As letras centrais não são um dígrafo específico: {letras_centrais}")

    





