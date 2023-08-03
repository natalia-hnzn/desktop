palavras = 'Paulo é d4veloper e um b0m musico'.split()

palavra_com_numeros = []

for palavra in palavras:
    tem_numero = any(c.isdigit() for c in palavra)
    if tem_numero:
        palavra_com_numeros.append(palavra)

print(palavra_com_numeros)
