class Contato:

    def __init__(self, nome, telefone, email):
        self.nome =  nome
        self.telefone = telefone
        self.email = email

    def atualizar_telefone(self, telefone):
        self.telefone = telefone

    def atualizar_email(self, email):
        self.email = email
