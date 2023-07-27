consoantes = []

for letras in range(10):
    letra = input('Digite uma letra: ')
    if letra not in 'aeiou':
        consoantes.append(letra)
    else:
        continue

print(consoantes)

