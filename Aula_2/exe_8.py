def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite u número inteiro.")


lista = []

for numero in range(1, 7):
    lista.append(obter_numero())

print(f"O maior número informado foi {max(lista)}, e o menor {min(lista)}")
