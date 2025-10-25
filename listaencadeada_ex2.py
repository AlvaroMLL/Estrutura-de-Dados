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
        if self.vazia():
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
    
    def remover_final(self):
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
            a.prox = None
        return item
    
    def remover_inicio(self):
        if self.vazia():
            return None
        
    
#programa principal
"""Utilizando a classe Lista criada na questão 1, faça um programa que leia
o nome e o sexo de vários animais. Se o animal for do sexo masculino,
insira o seu nome em uma lista chamada MACHOS. Caso contrário, insira
o nome numa lista chamada FEMEAS. Escolha uma condição de parada
para a entrada de dados a seu gosto. Ao final, devem ser exibidas as duas
listas criadas."""

machos = Lista()
femeas = Lista()
while True:
    print('[1] CADASTRAR ANIMAL')
    print('[2] MOSTRAR LISTA DOS MACHOS')
    print('[3] MOSTRAR LISTA DAS FEMEAS')
    print('[4] SAIR')
    op = int(input('DIGITE SUA OPÇÃO: '))
    if op == 1:
        nome = (input('Nome: '))
        sexo = (input('Sexo: '))
        sexo = sexo.upper()
        if sexo == 'MACHO':
            machos.inserir_final(nome)
        elif sexo == 'FEMEA':
            femeas.inserir_final(nome)
        else:
            print('Sexo inválido')
    elif op == 2:
        machos.imprimir()
    elif op == 3:
        femeas.imprimir()
    elif op == 4:
        break
    else:
        print('OPÇÃO INÁVLIDA')
machos.imprimir()
femeas.imprimir()