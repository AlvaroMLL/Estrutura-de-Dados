class Conta_Corrente:
    def __init__(self, num, titular):
        self.__num = num
        self.__saldo = 0
        self.__titular = titular
        self.__historico = []

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        self.__num = num

    @property
    def saldo(self):
        return self.__saldo
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo Insuficiente")
        else:   
            self.__saldo -= valor
            self.__historico.append(f'Saque: R$ {valor}')
    def depositar(self, valor):
        self.__saldo += valor
        self.__historico.append(f'Depósito: R$ {valor}')

    @property
    def titular(self):
        return self.__titular
    
    @property
    def historico(self):
        return self.__historico
    
    def imprimir_historico(self):
        print('Histórico de Lançamentos:')
        n = 1
        for lancamento in self.__historico:
            print(n, lancamento)
            n += 1

    #def __str__(self):
    #    return f'A conta de {self.titular} tem o número {self.#num} com o saldo de {self.saldo} R$' 

conta1 = Conta_Corrente(1234, "Álvaro")

#print(conta1)

print(f'Conta número: {conta1.num}, Títular: {conta1.titular} Saldo: R$ {conta1.saldo}')

conta1.depositar(500)

print(f'Conta número: {conta1.num}, Títular: {conta1.titular} Saldo: R$ {conta1.saldo}')

conta1.sacar(300)

print(f'Conta número: {conta1.num}, Títular: {conta1.titular} Saldo: R$ {conta1.saldo}')

conta1.sacar(800)
 
conta1.imprimir_historico()

