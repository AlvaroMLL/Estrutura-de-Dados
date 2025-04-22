class Aluno:
    def __init__(self, nome, disciplina):
        self.__nome = nome
        self.__disciplina = disciplina

    @property #get
    def nome(self):
        return self.__nome
    
    @nome.setter #set
    def nome(self,novo_nome):
        self.__nome = novo_nome
    
    @property #get
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter #set
    def disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina
    
    def __str__(self):
        return f'Aluno: {self.__nome} - Disciplina: {self.__disciplina}'

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
        return f'{self.__nome} ({self.__carga_horaria}h)'


disciplina = Disciplina('Estrutura de Dados',67)
aluno1 = Aluno('João da Silva', disciplina)
aluno2 = Aluno('Álvaro', disciplina)
aluno1.disciplina.nome = 'Banco de Dados I'
#print(disciplina)
#print(aluno.disciplina)
print(f'Aluno 1: {aluno1}')
print(f'Aluno 2: {aluno2}')
#aluno.disciplina.nome = 'Banco de Dados I'
# ou disciplina.nome = 'Banco de Dados I'
#print(aluno)


    

    