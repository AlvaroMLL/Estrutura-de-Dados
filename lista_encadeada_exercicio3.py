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

class Lista:
    def __init__(self):
        self.__inicio = None
        
    def vazia(self):
        return self.__inicio == None
    
    def primeiro(self):
        if self.vazia():
            return None
        return self.__inicio.dado
    
    def ultimo(self):
        p = self.__inicio
        if p == None:
            return None
        while p.prox != None:
            p = p.prox
        return p.dado
    
    def posicao(self, item):
        if self.vazia:
            return None
        n = 1
        p = self.__inicio
        while p != None:
            if p.dado == item:
                return n
            p = p.prox
            n += 1
        return None
    
    def elemento(self, pos):
        n = 1
        p = self.__inicio
        while p!= None:
            if pos == n:
                return p.dado
            p = p.prox
            n += 1
        return None
    
    def imprimir(self):
        p = self.__inicio
        print('Lista:',end=' ')
        if self.vazia():
            print('vazia')
            return
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

    def inserir_inicio(self, item):
        novo = No(item)
        novo.prox = self.__inicio
        self.__inicio = novo

    def inserir_final(self, item):
        novo = No(item)
        p = self.__inicio
        if p == None:
            self.__inicio = novo
            return
        while p.prox != None:
            p = p.prox
        p.prox = novo
    
    def remover_final (self):
        if self.vazia():
            return None
        a = None
        p = self.__inicio
        while p.prox != None:
            a = p
            p = p.prox
        item = p.dado
        if self.__inicio.prox == None:
            self.__inicio = None
        else:
            a.prox == None
        return item
    
#Programa

import random
L1 = Lista()
L2 = Lista()
L3 = Lista()
L4 = Lista()
for i in range(3):
    L1.inserir_final(random.randint(0,100))
    L2.inserir_final(random.randint(0,100))
L1.imprimir()
L2.imprimir()
for i in range(L1.tamanho()):
    item = L1.elemento(i + 1)
    L3.inserir_final(item)
L3.imprimir()
for i in range(L2.tamanho()):
    item = L2.elemento(i + 1)
    L3.inserir_final(item)
L3.imprimir()
for i in range(L3.tamanho()):
    item = L3.elemento(i + 1)
    L4.inserir_inicio(item)
L4.imprimir()
