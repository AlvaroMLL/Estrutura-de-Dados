class ContaCorrente:
    def __init__(self, numero):
        self.numero = numero
        self.__saldo = 0.00

    @property #get
    def numero(self):
        return self.__numero

    @numero.setter #set        
    def numero(self):
        return self.__numero

    @property #get
    def saldo(self):--
        return self.__saldo

    def depositar(self,numero):
        return 

    def sacar

    def __str__(self):
        return f'Numero da conta:{conta.__numero} Saldo: R${conta.saldo:.2f}'