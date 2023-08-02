palavra = input("Digite uma palavra: ")

print(f"A palavra é um palíndromo!") if palavra == palavra[::-1] else print(f"A palavra não é um palíndromo: {palavra} != {palavra[::-1]}")
