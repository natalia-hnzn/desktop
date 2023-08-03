from exe_4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)

for numero in numeros:
    print(f'{len(str(numero))} caracteres')
