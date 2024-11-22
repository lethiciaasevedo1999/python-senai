class Livro:
    #Iniciando meu método construtor
    def __init__(self, titulo, autor):
        #Especificando meus atributos
        self.titulo = titulo
        self.autor = autor
        
    def exibirLivro(self):
        print("*"*20)
        print("   LISTA DE LIVROS      ")
        print("*"*20)
        print(
              f"Título: {self.titulo}\n"
              f"Autor: {self.autor}")
        
    
titulo = input("Insira o nome do livro: ")
autor = input("Insira o nome do autor: ")

livro = Livro(titulo, autor)
livro.exibirLivro()
        