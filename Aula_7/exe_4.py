class Produto():

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd


class Cart:

    def __init__(self):
        self.produtos =[]

    def adicionar_produto(self, produto: Produto):
        self.produtos.append(produto)

    def calcula_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco * produto.qtd
        return total

    def mostrar_itens(self):
        if len(self.produtos) > 0:
            for i in self.produtos:
                print(f'Item {i.nome} qtd {i.qtd} valor R${i.preco}')
        else:
            print('Não existe mais itens no carrinho')


carrinho = Cart()
prod1 = Produto('Café', 35, 120)
prod2 = Produto('Chocolate', 7.5, 300)
carrinho.adicionar_produto(prod1)
carrinho.adicionar_produto(prod2)
carrinho.mostrar_itens()
print(f'O valor total do carrinho é R${carrinho.calcula_total()}')
