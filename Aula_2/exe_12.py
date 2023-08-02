def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número inteiro.")


numero = obter_numero()

if numero == 0:
    print("O número informado é zero!")
elif numero > 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")
