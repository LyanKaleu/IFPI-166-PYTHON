# 5. Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais
# alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos. Considerar a
# altura arredondando para duas casas decimais.

def calcular_media_altura(alunos):
    total_altura = qtd_alunos = 0

    for aluno in alunos:
        total_altura += aluno[2]
        qtd_alunos += 1

    media = total_altura / qtd_alunos
    return media


def alunos_menor_que_media(alunos, media):
    alunos_menor = []

    for aluno in alunos:
        if aluno[1] > 13 and round(aluno[2], 2) < round(media, 2):
            alunos_menor.append(aluno)

    return alunos_menor


def main():
    alunos = []

    for indice in range(30):
        nome = input(f"Digite o nome do aluno {indice+1}: ").strip()
        idade = int(input(f"Digite a idade do aluno {indice+1}: ").strip())
        altura = float(input(f"Digite a altura do aluno {indice+1} (em metros): ").strip())
        alunos.append([nome, idade, altura])

    media_altura = calcular_media_altura(alunos)
    alunos_abaixo_media = alunos_menor_que_media(alunos, media_altura)

    if alunos_abaixo_media:
        print("\nMAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA")
        for aluno in alunos_abaixo_media:
            print(f"-> {aluno[0]}")
    else:
        print("-> Nenhum aluno com mais de 13 anos tem altura abaixo da média.")


if __name__ == '__main__':
    main()
