dicionario = { 'nome': 'João', 'idade': 21, 'cidade': 'São Paulo'}
dicionario2 = {'email': 'lethicia@hotmail.com'}

# Mesclando diconários
dicionario.update(dicionario2)
print(dicionario)

dicionarioComposto = {('nome', 'sobrenome'): 'Lethicia', 'idade': 25}
print(dicionarioComposto)

#Excluindo o dicionário
dicionario.clear()
print(dicionario)