class Produto():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Estoque():

    def __init__(self):
        self.produtos = []

    def __add__(self, produto):
        self.produtos.append(produto)

