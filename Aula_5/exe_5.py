notas = input('Digite as 4 notas separadas por espaço: ').split()
soma_notas = 0

for nota in notas:
    soma_notas += float(nota)

media = soma_notas/len(notas)

if media >= 7:
    print(f'Aprovado com a média {media:.2f}')
else:
    prova_final = float(input('Digite a nota da prova final: '))
    media_final = (prova_final+media) / 2
    if media_final >= 5:
        print(f'Aprovado com média {media_final}')
    else:
        print('Reprovado')
