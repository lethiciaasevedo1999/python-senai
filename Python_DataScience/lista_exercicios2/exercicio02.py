#2)	Uma empresa de transporte público quer fazer um sistema automático
#  para identificar se o usuário terá gratuidade no transporte ou não. 
# Faça um programa que pergunte a idade do usuário, se ele tiver 65 anos 
# ou mais irá informar que ele tem gratuidade no transporte.

idadeUsuario = int(input("Qual a sua idade por favor? : "))

if idadeUsuario >= 65:
    print("Que legal, você tem direito a gratuidade no transporte, boa viagem :)")
else:
    print("Que pena, você ainda não tem direito a gratuidade no transporte. Obrigado ;)")