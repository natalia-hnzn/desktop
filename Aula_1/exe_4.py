tamanho = float(input("Qual o tamanho do arquivo em MB? "))
velocidade = float(input("Qual a velocidade da internet em Mbps? "))

print(
    f"O download do arquivo levará {round((tamanho/(velocidade/8))/60,2)} minutos para conclusão."
)
