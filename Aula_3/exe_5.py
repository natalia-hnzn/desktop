from exe_4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(10)
#print(f'Lista de números aleatórios: \n {numeros}')

for numero in numeros:
    if numero % 5 == 0:
        print(f'Número múltiplo de 5: {numero}')
        if numero < 95:
            print(f'Número {numero} menor que 95')
            pass
        elif numero < 150:
            print(f'Número {numero} maior que 150')
            pass
        elif numero > 1500:
            break
        else:
            continue
