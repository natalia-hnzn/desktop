def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite u número inteiro.")


num_1 = obter_numero()
num_2 = obter_numero()

print(f"\nA soma dos números é: {num_1+num_2}")
