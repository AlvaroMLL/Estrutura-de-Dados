class Disciplina:
    def __init__(self, nome, carga_horaria):
        self.__nome = nome
        self.__carga_horaria = carga_horaria
    
    @property #get
    def nome(self):
        return self.__nome
    
    @nome.setter #set
    def nome(self,novo_nome):
        self.__nome = novo_nome
    
    @property
    def carga_horaria(self):
        return self.__carga_horaria
    @carga_horaria.setter
    def carga_horaria(self, nova_carga_horaria):
        self.__carga_horaria = nova_carga_horaria

    def __str__(self):
        return f'{self.__nome} ({self.carga_horaria}h)'

    def __str__(self):
        return f'Aluno: {self.__nome} \nDisciplina: {self.__disciplina}'
disciplina = Disciplina('Estrutura de Dados',67)
aluno = Aluno('João da Silva', disciplina)
print(disciplina)
print(aluno)

