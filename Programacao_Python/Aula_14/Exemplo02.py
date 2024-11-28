dicionario = { 'nome': 'João', 'idade': 21, 'cidade': 'São Paulo'}

#Verificando se existe uma determinada chave
if 'nome' in dicionario:
    print("A chave 'nome' existe." )
    
#Usando o método get() para retornar um valor
idade = dicionario.get('idade')
print(idade)

#Método keys() para acessar as chaves disponíveis para acessar
chaves = dicionario.keys()
print(chaves)

#Método values() para acessar os valores guardados dentro das chaves
valores = dicionario.values()
print()