def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")


numero = obter_numero()
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
