import math


def calcular_tintas(area):
    litros = area/3
    latas = math.ceil(litros/18)
    return latas


area_a_pintar = float(input('Digite a área em metros quadrados: '))
total_latas = calcular_tintas(area_a_pintar)

print(f'Serão necessárias {total_latas} latas de tinta, pagando um total de {(total_latas * 80):.2f}')
