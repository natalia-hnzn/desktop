class Produto():

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def add_produto(self, qtd):
        self.qtd += qtd

    def remover_produto(self, qtd):
        if qtd <= self.qtd:
            self.qtd -= qtd
        else:
            print('Quantidade insuficiente')

    def valor_total(self):
        return self.preco * self.qtd


produto_1 = Produto('chocolate', 7.5, 3)
produto_1.add_produto(5)
produto_2 = Produto('Cookie', 5.25, 9)
estoque = [produto_1, produto_2]


total_estoque = 0

for produto in estoque:
    total_estoque += produto.valor_total()

print(f'O valor total de todos os produtos no estoque é: {total_estoque}')
