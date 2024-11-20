'''Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e
tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA. Caso contrário,
imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)'''

nome = input("Digite o seu nome completo: ")
sexo = input('''Digite o seu sexo:\n
             F para Feminino\n
             M para Masculino\n''')
idade = int(input("Digite sua idade: "))

print("*********************************************")
if sexo == "F" or sexo == "f" and idade < 25:
    print(f"Nome: {nome}\n"
          f"Status: ACEITA")  
else: 
    print(f"Nome: {nome}"
          f"Status: NÃO ACEITA")