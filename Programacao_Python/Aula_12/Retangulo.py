class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def calcularArea(self):
        return self.largura * self.altura
    def calcularPerimetro(self):
        return 2* (self.largura + self.altura)
    
altura = int(input("Insira a altura: "))
largura = int(input("Insira a largura do retângulo: "))

retangulo = Retangulo(largura, altura)
print(f"A área do retângulo é: {retangulo.calcularArea()}")
print(f"O perímetro do retângulo é: {retangulo.calcularPerimetro()}")



