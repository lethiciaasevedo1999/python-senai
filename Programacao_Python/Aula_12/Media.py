class Media:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2
        
    def calculoMedia(self):
        return (self.nota1 + self.nota2) / 2
        
nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))

resultado = Media(nota1, nota2)
print(f"A média é: {resultado.calculoMedia()}")