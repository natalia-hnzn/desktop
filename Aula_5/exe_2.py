def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite u número inteiro.")


number = obter_numero()

print(f'{number:.2f}')
