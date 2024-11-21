#Iniciando com Programação Orientada a Objetos em Python

#Definindo e criando a classe carro

class Carro:
 #Definindo o método construtor e seus atributos   
    def __init__(self, modelo, cor): #Inicializando os atributos do meu carro
        self.modelo = modelo
        self.cor = cor
 #Definindo a função para exibir       
    def mostrarInfo(self): #Mostrando a informação do meu carro
        print(f"Modelo: {self.modelo}\n"
              f"Cor: {self.cor}")

#Instanciando o objeto da classe
#Instanciar significa o objeto em si, então aqui, estou colocando o carro em ação
car = Carro("Fusca", "Azul")
car.mostrarInfo()
