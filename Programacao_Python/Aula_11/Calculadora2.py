#Resolução professor

class Calculadora: 
    
    def __init__(self):
        self.total = 0
        
    def iniciarCalculadora(self):
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        opcao = input("Digite a operação: ")
        
        if opcao == "+":
            self.somar(num1, num2)
        elif opcao == "-":
            self.subtrair(num1, num2)
        elif opcao == "*":
            self.multiplicar(num1, num2)
        elif opcao == "/":
            self.dividir(num1, num2)
        else:
            print("Opção inválida")
            
    def somar(self, num1, num2):
        self.total = num1 + num2
        print(f"Total: {self.total}")
    def subtrair(self, num1, num2):
        self.total = num1 - num2
        print(f"Total: {self.total}")
    def multiplicar(self, num1, num2):
        self.total = num1 * num2
        print(f"Total: {self.total}")
    def dividir(self, num1, num2):
        try:
            self.total = num1 / num2
            print(f"Total: {self.total}")
        except:
            print("Valor inválido")
        self.total = num1 / num2
        print(f"Total: {self.total}")
        
print("="*20)
print("CALCULADORA")
calculadora = Calculadora()
calculadora.iniciarCalculadora()
print("="*20)   
        