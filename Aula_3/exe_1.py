lista_nomes = ['Emanoela', 'Jonatan', '', 'Kelly', None, 'Henrique', '']

for i in lista_nomes:
    if not i:
        lista_nomes.remove(i)

print(lista_nomes)

# lista_nomes = [nome for nome in lista_nomes if nome and nome.split()]
