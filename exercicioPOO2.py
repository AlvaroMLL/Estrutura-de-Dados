class Aluno:
    def __init__(self, matricula, nome, notas = []):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    
    @property
    def matricula(self):
        return f'{self.__matricula}'
    
    @property 
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome
    
    @property
    def notas(self):
        return self.__notas

    def adiciona_notas(self, nota):
        self.__notas.append(nota)
    
    def media(self):
        total = self.__notas[0] + self.__notas[:]
        return total / len(self.__notas)
    
aluno = Aluno(20242370037, 'Álvaro', [100,70,30])
print(aluno)
aluno.adiciona_notas(80)
print(aluno)
