def fibonacci(tamanho):
    sequencia = [0, 1]
    for i in range(2, tamanho):
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia


numeros_fibonacci = fibonacci(15)
print(numeros_fibonacci)
