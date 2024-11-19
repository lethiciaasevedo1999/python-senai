#Validação de CPF com função 

#Função que calcula o primeiro dígito
def calcular_primeiro_digito(cpf):
    pesos = [10,9,8,7,6,5,4,3,2]
    soma = sum(int(cpf[i]) * pesos[i] for i in range(9))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

#Calculando o segundo dígito
def calcular_segundo_digito(cpf):
    pesos = [11, 10, 9, 8, 7, 6, 5 , 4, 3, 2]
    soma = sum(int(cpf[i]) * pesos[i] for i in range(10))
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

#Função para validar o CPF 
def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "") #substituindo pontos e ífens por strings
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    digito1 = calcular_segundo_digito(cpf)
    digito2 = calcular_segundo_digito(cpf)
    
    return cpf[-2:] == f"{digito1}{digito2}"

cpfValido = "441.586.068-02"
cpfInvalido = "324.331.456-01"

print(validar_cpf(cpfValido))
print(validar_cpf(cpfInvalido))