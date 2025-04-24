class Motor:
    def __init__(self, motorizacao, combustivel='flex'):
        self.__motorizacao = motorizacao 
        self.__combustivel = combustivel
    
    def get_motorizacao(self):
        return self.__motorizacao
    
    def get_combustivel(self):
        return self.__combustivel
    
    def set_motorizacao(self, nova_motorizacao):
        self.__motorizacao = nova_motorizacao
    
    def set_combustivel(self, novo_combustivel):
        self.__combustivel = novo_combustivel
    
    def __str__(self):
        return f'Motorização: {self.__motorizacao}L, Combustível: {self.__combustivel}'

motor = Motor('1,6') 
#print(motor)        
#combustivel padrao é 'Flex'

class Dimensao:
    def __init__(self, altura, largura, comprimento):
        self.__altura = altura
        self.__largura = largura
        self.__comprimento = comprimento
    
    def get_altura(self):
        return self.__altura
    
    def get_largura(self):
        return self.__largura
    
    def get_comprimento(self):
        return self.__comprimento
    
    def set_altura(self, nova_altura):
        self.__altura = nova_altura
    
    def set_largura(self, nova_largura):
        self.__largura = nova_largura

    def set_comprimento(self, novo_comprimento):
        self.__comprimento = novo_comprimento

    def __str__(self):
        return f'Altura: {self.__altura}, Largura: {self.__largura}, Comprimento: {self.__comprimento}'
    
dimensao = Dimensao(1.67, 1.81, 4.37)
#print(dimensao)  

class Carro:
    def __init__(self, cor, placa, motor, dimensao):
        self.__cor = cor
        self.__placa = placa
        self.__motor = motor 
        self.__dimensao = dimensao
    
    def get_cor(self):
        return self.__cor

    def get_placa(self):
        return self.__placa
    
    def set_placa(self, nova_placa):
        self.__placa = nova_placa
    
    def get_motor(self):
        return self.__motor

    def get_dimensao(self):
        return self.__dimensao

    def __str__(self):
        return f'Cor: {self.__cor}, Placa: {self.__placa} \nMotor: {self.__motor}, \nDimensao: {self.__dimensao}'

carro = Carro('Preto', 'XXX1234', motor, dimensao)
print (carro)

#Transformar para @property = get
# e @placa.setter = set