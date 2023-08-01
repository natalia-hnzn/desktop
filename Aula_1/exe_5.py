def obter_numero_alunos(turma_num):
    while True:
        try:
            num_alunos = int(
                input(f"Digite a quantidade de alunos da turma {turma_num}: ")
            )
            if num_alunos <= 0:
                print("A quantidade de alunos deve ser maior que zero.")
            elif num_alunos > 40:
                print("A quantidade de alunos não pode ser maior que 40.")
            else:
                return num_alunos
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")


def calcular_media_alunos_por_turma(num_turmas):
    total_alunos = 0
    for i in range(1, num_turmas + 1):
        num_alunos = obter_numero_alunos(i)
        total_alunos += num_alunos

    media_alunos_por_turma = total_alunos / num_turmas
    return media_alunos_por_turma


while True:
    try:
        num_turmas = int(input("Digite a quantidade de turmas: "))
        if num_turmas <= 0:
            print("A quantidade de turmas deve ser maior que zero.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

media_alunos = calcular_media_alunos_por_turma(num_turmas)
print(f"A média de alunos por turma é: {media_alunos:.2f}")
