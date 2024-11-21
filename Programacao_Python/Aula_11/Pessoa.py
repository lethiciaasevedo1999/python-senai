
class Pessoa:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
    def mostrarInfo(self):
        print(f"Nome: {self.nome}\n"
              f"Endereço: {self.endereco}\n"
              f"Telefone: {self.telefone}")
        
pessoa = Pessoa ("Lethicia", "Rua Marco Polo, 142 - Prq. Boturussu", "(11)958754595")
pessoa.mostrarInfo()

print("*************************************************************")

nome = input("Digite seu nome completo: ")
endereco = input("Digite seu endereço: ")
telefone = input("Digite aqui seu telefone com DDD: ")

humano = Pessoa(nome, endereco, telefone)
print("------Exibindo os dados------")
humano.mostrarInfo()

