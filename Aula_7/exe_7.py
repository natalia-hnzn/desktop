class Tarefa:

    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data
        self.concluida = False

    def concluir_tarefa(self):
        self.concluida = True

    def exibir_detalhes(self):
        print(f'A tarefa {self.descricao} é do dia {self.data} e está '
            f'{"concluida" if self.concluida else "não concluída"}')


tarefa = Tarefa('Exe POO', '16/08')
tarefa.exibir_detalhes()
tarefa.concluir_tarefa()
tarefa.exibir_detalhes()
