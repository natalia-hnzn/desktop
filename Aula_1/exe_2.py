str_1 = input('Digite a primeira frase: ')
str_2 = input('Digite a segunda frase: ')

print(f'Tamanho de {str_1}: {len(str_1)} caracteres\nTamanho de {str_2}: {len(str_2)} caracteres')

if len(str_1) != len(str_2):
    print('As duas strings são de tamanhos diferentes')
else:
    print('As duas strings possuem o mesmo tamanho')


if str_1 == str_2:
    print('As duas strings possuem o mesmo conteúdo')
else:
    print('As duas strings possuem conteúdo diferente')
