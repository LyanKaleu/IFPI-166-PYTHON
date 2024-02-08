# 3. Escreva um programa que ler a nota de 50 alunos. Mostre uma lista apenas com os índices dos alunos que
# tem nota maior ou igual a 6 (seis).

def ler_notas():
    notas = []
    print("Digite as notas dos 50 alunos:")
    for i in range(50):
        notas.append(float(input().strip()))  # Lê as notas dos 50 alunos fornecidas pelo usuário

    return notas


def determinar_alunos_maior_que_6(notas):
    alunos_maior_que_6 = []
    for i in range(50):
        if notas[i] >= 6:
            alunos_maior_que_6.append(i)  # Adiciona o índice do aluno à lista se a nota for maior ou igual a 6

    return alunos_maior_que_6


def main():
    lista_original = ler_notas()  # Chama a função para ler as notas dos 50 alunos
    lista_alunos = determinar_alunos_maior_que_6(lista_original)  # Chama a função para determinar os alunos aprovados
    print("Lista de índices dos alunos com nota maior ou igual a 6:", lista_alunos)  # Imprime a lista de índices dos alunos aprovados


if __name__ == '__main__':
    main()  # Chama a função principal
