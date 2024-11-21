'''Entrar com nome, nota da PR e nota da PR2 de um aluno. Imprimir nome, nota
da PR1, nota da PR2, média e uma das mensagens: Aprovado, Reprovado ou em
Prova Final (a média é 7 para aprovação, menor que 3 para reprovação e as de-
mais em prova final).'''

nome = input("Digite seu nome completo: ")
notaPr1 = float(input("Digite a nota da PR1: "))
notaPr2 = float(input("Digite a nota da PR2: "))
media = (notaPr1 + notaPr2) / 2

if media >= 7:

    print(
        "******************************\n"
        "        Sistema Aluno\n         "
        "******************************\n"
          f"Nome do aluno: {nome}\n"
          f"Nota PR1: {notaPr1}\n"
          f"Nota PR2: {notaPr2}\n"
          
        '''Status: PARABÉNS ! Você foi APROVADO.''')
elif media < 3:
    print(
        "******************************\n"
        "        Sistema Aluno\n         "
        "******************************\n"
          f"Nome do aluno: {nome}\n"
          f"Nota PR1: {notaPr1}\n"
          f"Nota PR2: {notaPr2}\n"
          
        '''Status: Você foi reprovado, que pena :( ''')
else:
    print(
        "******************************\n"
        "        Sistema Aluno\n         "
        "******************************\n"
          f"Nome do aluno: {nome}\n"
          f"Nota PR1: {notaPr1}\n"
          f"Nota PR2: {notaPr2}\n"
          
        '''Status: Você está de recuperação, estude mais !''')
