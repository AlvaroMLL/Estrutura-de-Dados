class No:
    def __init__(self, dado):
        self.__dado = dado
        self.__prox = None

    @property
    def dado(self):
        return self.__dado
    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def prox(self):
        return self.__prox
    @prox.setter
    def prox(self, prox):
        self.__prox = prox

class Pilha:
    def __init__(self):
        self.__topo = None

    def vazia(self):
        return self.__topo == None

    def elem_topo(self):
        if self.vazia():
            return None
        return self.__topo.dado

    def empilhar(self, item):
        novo = No(item)
        novo.prox = self.__topo
        self.__topo = novo

    def desempilhar(self):
        if self.vazia():
            return None
        item = self.__topo.dado
        self.__topo = self.__topo.prox
        return item

    def imprimir(self):
        p = self.__topo
        print('Pilha:',end=' ')
        if self.vazia():
            print('vazia')
            return
        while p != None:
            print(p.dado, end=' ')
            p = p.prox
        print()

    def tamanho(self):
        n = 0
        p = self.__topo
        while p != None:
            n += 1
            p = p.prox
        return n

    def esvaziar(self):
        self.__topo = None

    def somar(self):
        s = 0
        p = self.__topo
        while p != None:
            s += p.dado
            p = p.prox
        return s

pilha = Pilha()
pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.imprimir()
print('Soma:', pilha.somar())
print('Tamanho:', pilha.tamanho())
pilha.desempilhar()
pilha.imprimir()
print('Tamanho:', pilha.tamanho())
pilha.esvaziar()
pilha.imprimir()
print('Tamanho:', pilha.tamanho())
