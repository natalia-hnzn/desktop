def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")


primeiro = obter_numero()
contador = primeiro + 1

while contador <= primeiro + 10:
    print(contador)
    contador += 1
