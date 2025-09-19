class Aluno:
    def __init__(self, matr, periodo, nome):
        self.matr = matr
        self.periodo = periodo
        self.nome = nome

aluno1 = Aluno(1111, 3, "Joao")
aluno2 = Aluno (2222, 1, "Matheus")
print (f"Aluno {aluno1.nome} tem a matrícula {aluno1.matr} e está no {aluno1.periodo} periodo")
print (f"Aluno {aluno2.nome} tem a matrícula {aluno2.matr} e está no {aluno2.periodo} periodo")