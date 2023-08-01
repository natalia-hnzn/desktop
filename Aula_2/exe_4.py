def obter_raio():
    while True:
        entrada = input("Digite o raio do círculo: ")
        try:
            raio = float(entrada)
            return raio
        except ValueError:
            print("Entrada inválida, informe um número.")


raio = obter_raio()

print(f"A área do círculo é: {round(3.14159*(raio**2), 2)}")
