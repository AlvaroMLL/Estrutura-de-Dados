class Pais:
    def __init__(self, nome, capital, dimensao):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteiras = []
    @property
    def nome(self):
        return self.__nome
    
    @property
    def capital(self):
        return self.__capital
    
    @property
    def dimensao(self):
        return self.__dimensao
    
    @property
    def fronteira(self):
        return self.__fronteiras
    
    def __str__ (self):
        for i in self.__fronteiras:
            paises =+ i.nome + ' ' 
        return f'Nome: {self.__nome}\nCapital: {self.__capital}\nDimensão : {self.__dimensao}\nFronteiras: {paises}'
    