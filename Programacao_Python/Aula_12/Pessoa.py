
class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
         
    def apresentar(self):
        print(f"Meu nome é: {self.nome} e minha idade é: {self.idade}") 
        
nome = input("Digite seu nome: ") 
idade = input("Digite a sua idade: ")          

garoto = Pessoa(nome, idade)
garoto.apresentar()