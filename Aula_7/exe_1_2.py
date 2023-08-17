class Produto():

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


class Estoque():
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def remover_produto(self, produto: Produto):
        self.produtos.remove(produto)

    def calcula_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.qtd
        return total


produto_1 = Produto('Chocolate', 7.5, 8)
produto_2 = Produto('Chocolate', 7.5, 8)
estoque = Estoque()
estoque.adicionar_produto(produto_1)
estoque.adicionar_produto(produto_2)
print(f'O valor total do estoque é: {estoque.calcula_total()}')
