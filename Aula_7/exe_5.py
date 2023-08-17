class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def realizar_deposito(self, valor):
        self.saldo += valor


conta = ContaBancaria(1234, 'Valéria')
print(f'A conta de {conta.titular} está aberta com saldo de {conta.saldo}')
conta.realizar_deposito(1234435.45)
print(f'A conta de {conta.titular} possui o saldo de {conta.saldo}')
