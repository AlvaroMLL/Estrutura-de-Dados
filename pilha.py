class Pilha:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0
    
    def topo(self):
        if self.vazia():
            return None # ou print('pilha vazia')
        else:
            ind = len(self.__itens) - 1
            return self.__itens[ind]
    
    def empilhar(self, dado):
        self.__itens.append(dado)
    
    def desempilhar(self):
        if self.vazia(): # ou print('pilha vazia')
            return None
        else:
            dado = self.__itens.pop()
            return dado
    
    def imprimir(self):
        for dado in self.__itens:
            print(dado, end='')
        print('<= topo')

    def __str__(self):
        return self.__itens.__str__()
#programa principal

p = Pilha()
p.imprimir
p.empilhar('A')
p.imprimir
p.empilhar('B')
p.imprimir
p.empilhar('C')
p.imprimir
p.desempilhar
p.imprimir

aux = Pilha()
while not p.vazia():
    dado = p.desempilhar
    aux.empilhar(dado)
    print(dado)

while not aux.vazia():
    dado = aux.desempilhar
    p.empilhar(dado)