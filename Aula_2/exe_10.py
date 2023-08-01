palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print(f"A palavra é um palíndromo!")
else:
    print(f"A palavra não é um palíndromo: {palavra} != {palavra[::-1]}")
