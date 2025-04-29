class Data:
    def __init__ (self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, novo_dia):
        self.__dia = novo_dia
    
    @property
    def mes(self):
        return self.__mes

    @dia.setter
    def mes(self, novo_mes):
        self.__mes = novo_mes
    
    @property
    def ano(self):
        return self.__ano
    @dia.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    def __str__(self):
        return f'{self.__dia:02}/{self.__mes:02}/{self.__ano}'
    
data = Data(14, 4, 2006)
print(data)