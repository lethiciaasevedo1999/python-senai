'''Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da
pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido.'''

anoNascimento = int(input("Digite o seu ano de nascimento : "))
anoAtual = int(input("Digite o ano atual: "))

if anoAtual < anoNascimento:
    print("Ano de nascimento inválido, tente novamente: ")
else : 
    idade = anoAtual - anoNascimento
    print(f"Você tem {idade} anos.")

