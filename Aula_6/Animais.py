from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    @abstractmethod
    def emitir_som(self):
        pass


class Cachorro(Animal):

    def __init__(self, raca, nome, especie):
        super().__init__(nome, especie)
        self.__raca = raca

    def set_raca(self, new_raca):
        self.__raca = new_raca

    def get_raca(self):
        return self.__raca

    def emitir_som(self):
        print(f'O cachorro {self.nome}, late.')


class Gato(Animal):

    def __init__(self, pelagem, nome, especie):
        super().__init__(nome, especie)
        self.__pelagem = pelagem

    def set_pelagem(self, new_pelagem):
        self.__pelagem = new_pelagem

    def get_pelagem(self):
        return self.__pelagem

    def emitir_som(self):
        print(f'O gato {self.nome}, mia.')


cachorro = Cachorro('Vira-Lata', 'Pipoca', 'Mamífero')
gato = Gato('Preta', 'Cake', 'Mamífero')

cachorro.set_raca('Vira-lata')
cachorro.emitir_som()
gato.emitir_som()
print(f'A raça do {cachorro.nome} é {cachorro.get_raca()}')
