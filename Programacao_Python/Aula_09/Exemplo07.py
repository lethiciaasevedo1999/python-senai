#Verificação

#Com strings
texto = "senai"

# "isalpha", verifica se possui apenas letras na palavra parâmetro
if(texto.isalpha()):
    print("Possu apenas letras")
else: 
    print("Não possui apenas letras")
    

# Com dígitos
texto2 = "123456"

#Verifica se possui apenas números no parâmetro
if(texto2.isdigit()):
    print("Possui apenas números")
else:
    print("Não possui apenas números")