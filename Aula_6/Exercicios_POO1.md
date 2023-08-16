Neste exercício, vamos criar um sistema simples de classes em Python para representar diferentes tipos de animais, aplicando os conceitos de herança e encapsulamento. Criaremos três classes: Animal, Cachorro e Gato. Cada classe terá atributos e métodos específicos.

Classe Animal: A classe base que representa um animal genérico. Esta classe terá os seguintes atributos e método:
Atributos:

- nome (string): O nome do animal.
- especie (string): A espécie do animal.
  Método:
- emitir_som(): Retorna uma mensagem genérica indicando que o animal emite um som.

Classe Cachorro (Subclasse de Animal): Uma classe que representa um cachorro. Esta classe terá os seguintes atributos e métodos, incluindo o uso de encapsulamento:
Atributos:

- \_\_raca (string): A raça do cachorro (encapsulado).
  Métodos:
- obter_raca(): Retorna a raça do cachorro.
- emitir_som(): Retorna uma mensagem específica indicando que o cachorro late.

Classe Gato (Subclasse de Animal): Uma classe que representa um gato. Esta classe terá os seguintes atributos e métodos, incluindo o uso de encapsulamento:
Atributos:

- \_\_pelagem (string): O tipo de pelagem do gato (encapsulado).
  Métodos:
- obter_pelagem(): Retorna o tipo de pelagem do gato.
- emitir_som(): Retorna uma mensagem específica indicando que o gato mia.
