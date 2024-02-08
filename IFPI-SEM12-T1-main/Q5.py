# 05. O dodô é uma ave não voadora, extinta atualmente, e que era endêmica da Ilha
# Maurítius, na costa leste da África. A partir do ano 1600, durante cada ano, 6%
# dos animais dos animais vivos no começo do ano morreram e o número de
# animais nascidos ao longo do ano que sobreviveram foi de 1% da população
# inicial.
# Escreva um programa que leia a população de aves no início do ano 1600 e
# imprime, anualmente, a partir do fim de 1600, o número de nascimentos, mortes e o total da população
# por ano (apenas a parte inteira do números, separados por vírgula). O programa encerra sua execução
# quanto a população total cai para menos de 10% da população original.

# Define a função para calcular as estatísticas de nascimentos, mortes e população.
def calcular_estatisticas_dodo(populacao):
    nascimentos = populacao / 100
    mortes = populacao / 100 * 6
    populacao = populacao + nascimentos - mortes

    return nascimentos, mortes, populacao


def main():
    # Define o ano inicial.
    ano = 1600
    # Solicita a população inicial ao usuário.
    populacao_inicial = int(input("Digite a população inicial em 1600: ").strip())
    # Define a população atual como a população inicial.
    populacao_atual = populacao_inicial

    # Loop continua enquanto a população atual for maior ou igual a 10% da população inicial.
    while populacao_atual >= 0.1 * populacao_inicial:
        # Chama a função para calcular as estatísticas.
        nascimentos, mortes, populacao_atual = calcular_estatisticas_dodo(populacao_atual)
        # Imprime as estatísticas arredondadas para o ano atual.
        print(f"Ano {round(ano)}, Nascimentos = {round(nascimentos)}, Mortes = {round(mortes)}, População atual = {round(populacao_atual)}")
        # Incrementa o ano.
        ano += 1


if __name__ == '__main__':
    main()
