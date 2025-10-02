class Pilha:
    def __init__(self):
        self.__itens = []
    
    def empilhar(self, dado):
        self.__itens.append(dado)
    
    def desempilhar(self):
        if len(self.__itens) == 0:
            return None
        else:
            dado = self.__itens.pop()
            return dado
    
    def exibir_topo(self):
        if len(self.__itens) == 0:
            return None
        else:
            ind = len(self.__itens) - 1
            return self.__itens[ind]
    
    def exibir_pilha(self):
        for dado in self.__itens:
            print(dado, end=' ')
    
    def tamanho_pilha(self):
        len(self.__itens)
    
    def esvaziar_pilha(self):
        self.__itens = []
    
p = Pilha()
while True:
    print('EDITOR DE PILHA')
    print('[1] EMPILHAR')
    print('[2] DESEMPLIHAR')
    print('[3] EXIBIR ELEMENTO DO TOPO')
    print('[4] EXIBIR A PILHA')
    print('[5] TAMANHO DA PILHA')
    print('[6] ESVAZIAR A PILHA')
    print('[0] SAIR')
    op = input('Digite sua opção: ')
    if op == '1':
        dado = input('Dado a ser empilhado: ')
        p.empilhar(dado)
    if op == '2':
        dado = p.desempilhar
        if dado == None:
            print('Erro: pilha vazia')
        else:
            print('Dado desempilhado: ', dado)
    if op == '3':
        dado = p
        if dado == None:
            print('Erro: pilha vazia')
        else:
            print('Topo: ', dado)
    if op == '4':
        print('Pilha: ', p.exibir_pilha())
    if op == '5':
        print('Tamanho da pilha: ', p.tamanho_pilha())
    if op == '6':
        p.esvaziar_pilha()
        print('Pilha esvaziada')
    if op == '0':
        False