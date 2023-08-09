from exe_4 import gera_numeros_aleatorios

numeros = gera_numeros_aleatorios(20)
numeros = [str(numero) for numero in numeros]
numeros_agrupados = ' '.join(numeros)
print(f'Os números da lista agrupados sem espaço geram a seguinte string: '
      f'\n {numeros_agrupados} ')
