class Aluno:
    def __init__(self, matr, nota, nome):
        self.__matr = matr
        self.__nota = nota
        self.__nome = nome
    
    @property
    def matr(self):
        return self.__matr
    

    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nota):
        if nota > 100 or nota < 0:
            print('Nota Inválida')
        else:
            self.__nota = nota

    @property
    def nome(self):
        return self.__nome
    
    #def __str__(self):
    #    return f'O aluno {self.nome} tem a matricula {self.#matr} e a nota {self.nota}'


aluno = Aluno(1111, 90, "Joao")

print(f'Aluno: {aluno.nome}, Matrícula: {aluno.matr}, Nota: {aluno.nota}')

aluno.nota = 60

print(f'Aluno: {aluno.nome}, Matrícula: {aluno.matr}, Nota: {aluno.nota}')

aluno.nota = 110

print(f'Aluno: {aluno.nome}, Matrícula: {aluno.matr}, Nota: {aluno.nota}')

aluno.nota = -10

print(f'Aluno: {aluno.nome}, Matrícula: {aluno.matr}, Nota: {aluno.nota}')