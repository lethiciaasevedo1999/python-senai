#Desafio de verificação de login e senha

def verificar_senha(senha):
    #Verifica se a senha contém pelo menos uma letra e pelo menos um número
    tem_letra = any(caractere.isalpha() for caractere in senha)
    tem_numero = any(caractere.isdigit() for caractere in senha)
    
    #Retorna True se ambas as condições forem atendidas
    return tem_letra and tem_numero

#Exemplos de uso:
senha1 = "abc123"
senha2 = "senha"
senha3 = "12345"
senha4 = "abc!@#"

print(verificar_senha(senha1)) #True, poios contém letras e números
print(verificar_senha(senha2)) #False, pois não contém números
print(verificar_senha(senha3)) #False, pois não contém letras
print(verificar_senha(senha4)) #False, pois contém caracteres especiais, mas não números
