class Eh_Quadrado:
    def __init__(self,altura,comprimento):
        self.altura = altura
        self.comprimento = comprimento
    def quadrado(self):
        if self.altura == self.comprimento:
            return True
        else:
            return False
        