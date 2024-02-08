# Função para calcular a média do aluno com base na matrícula
def calcular_media_aluno(matricula, alunos):
    if matricula in alunos:  # Verifica se a matrícula está presente no dicionário de alunos
        notas = alunos[matricula]['Notas']  # Obtém as notas do aluno pela matrícula
        media = sum(notas) / len(notas)  # Calcula a média das notas
        return media  # Retorna a média do aluno
    else:
        return None  # Retorna None se a matrícula não estiver presente no dicionário


def main():
    alunos = {}  # Dicionário para armazenar os dados dos alunos

    # Loop para cadastrar os alunos
    while True:
        matricula = input("Digite a matrícula do aluno (ou deixe em branco para parar): ").strip()

        if matricula == '':
            break

        nome = input("Digite o nome do aluno: ").strip()
        nota1 = float(input("Digite a nota 1 do aluno: ").strip())
        nota2 = float(input("Digite a nota 2 do aluno: ").strip())

        alunos[matricula] = {'Nome': nome, 'Notas': [nota1, nota2]}  # Armazena os dados do aluno no dicionário

    # Loop para calcular e mostrar a média dos alunos
    while True:
        matricula = input("Digite a matrícula do aluno para calcular a média (ou deixe em branco para parar): ").strip()

        if matricula == '':
            break

        media = calcular_media_aluno(matricula, alunos)  # Calcula a média do aluno

        if media is not None:
            print(f"Média de {alunos[matricula]['Nome']}: {media:.1f}")  # Mostra a média do aluno com uma casa decimal
        else:
            print(f"Matrícula {matricula} não encontrada.")  # Mostra uma mensagem se a matrícula não for encontrada


if __name__ == '__main__':
    main()  # Chama a função principal
