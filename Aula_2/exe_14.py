numeros = input('Insira uma lista de numeros separados por espaço: ').split()
numeros = [int(numero) for numero in numeros]
pares = [num for num in numeros if num % 2 ==0]
print(f'Os números pares são {pares}')

def obter_numero():
    while True:
        entrada = input("Digite um número: ")
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("Entrada inválida, digite u número inteiro.")


lista = []

for numero in range(0, 10):
    lista.append(obter_numero())

par = []

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        continue

print(
    f"A lista de números informada foi:\n{lista}\n Os pares contidos na lista são:\n{par}"
)
