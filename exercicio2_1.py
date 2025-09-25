class Retangulo:
    def __init__(self, larg, comp):
        self.__larg = larg
        self.__comp = comp

    @property
    def larg(self):
        return self.__larg
    
    @larg.setter
    def larg(self, larg):
        self.__larg = larg
    
    @property
    def comp(self):
        return self.__comp
    
    @comp.setter
    def comp(self, comp):
        self.__comp = comp

    def calcula_area(self):
        return self.larg * self.comp
    
    def eh_quadrado(self):
        return self.larg == self.comp
           
    def __str__(self):
        return f'O retangulo possui {self.larg} de largura e {self.comp} de comprimento'

ret = Retangulo(3,3)
print(ret)
print('Área do retângulo:', ret.calcula_area())
if ret.eh_quadrado():
    print('O retângulo é um quadrado')
else:
    print('O retangulo não é um quadrado')