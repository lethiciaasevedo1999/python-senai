'''A turma de Programação 1, por ter muitos alunos, será dividida em dias de provas.
Após um estudo feito pelo coordenador, decidiu-se dividi-la em três grupos.
Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá
fazer as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas
se encontram no bloco F:
    A - K:sala 101
    L-N:sala 102
    O - Z:sala 103'''

nome = input("Digite o seu nome completo: ")
primeiraLetra = (nome[0])

if primeiraLetra >= "A" and primeiraLetra <= "K":
    print("LOCAL DE PROVA:\n"
          "Bloco: F\n"
          "Sala: 101")
elif primeiraLetra >= "L" and primeiraLetra <= "N":
     print("LOCAL DE PROVA:\n"
          "Bloco: F\n"
          "Sala: 102")
elif primeiraLetra >= "O" and primeiraLetra <= "Z":
      print("LOCAL DE PROVA:\n"
          "Bloco: F\n"
          "Sala: 103")