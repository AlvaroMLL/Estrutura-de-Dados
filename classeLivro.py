class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__disponivel = disponivel
    
    @property
    def titulo(self):
        return self.__titulo
    @titulo.setter
    def titulo(self, titulo):
      self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
    
    @property
    def ano_publicacao(self):
        return self.__ano_publicacao
    @ano_publicacao.setter
    def ano_publicacao(self, ano_publicacao):
        self.__ano_publicacao = ano_publicacao
    
    def exibir_info(self):
        print(f'Título: {self.titulo}, Autor: {self.autor} Ano: {self.ano_publicacao}')
    
    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False 
            print('Livro esprestado')
        else:
            print('Livro já emprestado')

    def devolver(self):
        if self.__disponivel:
            print('Você já está com o livro')
        else:
            self.__disponivel = True
            print('Livro devolvido')
    
    def esta_disponivel(self):
        if self.__disponivel == True:
            print("Tá disponivel")
        else:
            print('Não está disponivel')

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)

livro1.exibir_info()
livro1.emprestar()
livro1.esta_disponivel()  # False
livro1.devolver()



    
    