
def peso_ideal(altura):
    return (72.7 * altura) - 58


altura = float(input('Informe sua altura:'))

print(f'O seu peso ideal é {peso_ideal(altura):.2f}kg')
