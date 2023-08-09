def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")


def par_impar(numero):
    if numero % 2 == 0:
        return True


numero = obter_numero()

print('Número par') if par_impar(numero) else print('Número ímpar')
