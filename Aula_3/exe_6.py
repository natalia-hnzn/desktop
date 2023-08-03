from exe_4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
# print(f'A lisa de números inicial é {numeros}')

for i in range(1, len(numeros), 2):
    print(f'Número {numeros[i]} no índice {i}')
