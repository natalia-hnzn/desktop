def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")

numero = obter_numero()

print('Par') if numero % 2 == 0 else print(('Impar'))
