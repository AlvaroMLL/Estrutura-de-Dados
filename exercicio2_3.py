class Conta_Corrente:
    def __init__(self, num, saldo, titular):
        self.__num = num
        self.__saldo = saldo
        self.__titular = titular

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def num(self, titular):
        self.__titular = titular

    #def __str__(self):
    #    return f'A conta de {self.titular} tem o número {self.#num} com o saldo de {self.saldo} R$' 

conta1 = Conta_Corrente(1234, 500000, "Álvaro")
conta2 = Conta_Corrente(4321, 400, "Roberto")

#print(conta1)
#print(conta2)

print(f'Conta número: {conta1.num}, Títular: {conta1.titular} Saldo: R$ {conta1.saldo}')

conta1.saldo = 320

print(f'Conta número: {conta1.num}, Títular: {conta1.titular} Saldo: R$ {conta1.saldo}')