class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        
    def exibir_preco(self):
        print(f"Preço final do {self.nome}: R${self.preco:.2f}")
        
produto = Produto("Camiseta", 50)
produto.aplicar_desconto(10)
produto.exibir_preco()


'''nomeProduto, preco 
colocar o percentual de desconto 
criar função que aplicar o desconto e depois
exibir o preço com o desconto'''