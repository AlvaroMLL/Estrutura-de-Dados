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

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__final = None

    def vazia(self):
        return self.__inicio == None

    def primeiro(self):
        if self.vazia():
            return None
        return self.__inicio.dado

    def inserir(self, item):
        novo = No(item)
        if self.vazia():
            self.__inicio = novo
            self.__final = novo
        else:
            self.__final.prox = novo
            self.__final = novo

    def remover(self):
        if self.vazia():
            return None
        item = self.__inicio.dado
        self.__inicio = self.__inicio.prox
        return item

    def imprimir(self):
        print('Fila:', end=' ')
        if self.vazia():
            print('vazia')
        else:
            p = self.__inicio
            while p != None:
                print(p.dado, end=' ')
                p = p.prox
            print()

    def tamanho(self):
        n = 0
        p = self.__inicio
        while p != None:
            n += 1
            p = p.prox
        return n

    def esvaziar(self):
        self.__inicio = None
        self.__final = None
