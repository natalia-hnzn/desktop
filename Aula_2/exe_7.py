def obter_temperatura():
    while True:
        entrada = input("Informe a temperatura em Celcius: ")
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite um número.")


temperatura = obter_temperatura()

print(f"A temperatura em Fahrenheit é {round((temperatura*(9/5))+32, 2)}°")
