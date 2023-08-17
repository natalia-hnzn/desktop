class Aluno:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__disciplinas = []

    def add_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    def mostrar_disciplinas(self):
        return self.__disciplinas


aluno = Aluno('Natalia', 28)
aluno.add_disciplina('Desenvolvimento Web')
aluno.add_disciplina('LPA')
print(f'O(a) aluno(a) {aluno.nome} cursa as disciplinas {", ".join(aluno.mostrar_disciplinas())}')

