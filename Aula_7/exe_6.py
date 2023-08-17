class Pedido:

    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data
        self.itens = []

    def adicionar_itens(self, item):
        self.itens.append(item)

pedido1 = Pedido('Primeiro pedido', ' 16/08/2023')
pedido1.adicionar_itens('Camisa')
pedido1.adicionar_itens('Calça')

print(f'Os items do pedido {pedido1.descricao} são:\n')
for i in pedido1.itens:
    print(i)
