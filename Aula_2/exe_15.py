def obter_fruta():
    fruta = input("Digite o nome da fruta: ")
    return fruta


def obter_numero():
    while True:
        entrada = input("Digite a quantidade: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")


def set_frutas():
    frutas = {}
    for i in range(5):
        fruta = str(obter_fruta()).capitalize()
        quantidate = obter_numero()
        frutas[fruta] = quantidate
    return frutas


dicionario_frutas = set_frutas()

for fruta, quantidade in dicionario_frutas.items():
    print(f"{fruta}: {quantidade}")
