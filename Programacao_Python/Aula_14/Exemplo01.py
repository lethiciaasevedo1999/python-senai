# Criando o meu dicionário
dicionario = { 'nome': 'João', 'idade': 21, 'cidade': 'São Paulo'}
print(dicionario)

# Acesando valor no dicionário
print(dicionario['nome'])

# Alterando valor no dicionário
dicionario['idade'] = 30
print(dicionario)

# Adicionando uma nova chave no dicionário
dicionario['profissao'] = 'engenheiro'
print(dicionario)

#Removendo um valor do dicionário
del dicionario['cidade']
print(dicionario)