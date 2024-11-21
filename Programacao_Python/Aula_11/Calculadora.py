#Calculadora POO

class Calculadora: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    
    def adicao(self):
        return self.x + self.y

    def subtracao(self):
        return self.x - self.y
    
    def multiplicacao(self):
        return self.x * self.y
    
    def divisao(self):
        return self.x / self.y
          
 
    def mostrarInfo(self):
        print(f"Adição: {self.adicao()}")
        print(f"Subtração: {self.subtracao()}")
        print(f"Multiplicação: {self.multiplicacao()}")
        print(f"Divisão: {self.divisao()}")
 
calculadora = Calculadora(15, 5)
calculadora.mostrarInfo()
