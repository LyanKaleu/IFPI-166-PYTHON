# 03. Dado um país A, com taxa de natalidade de 2% ao ano, e um país B com uma taxa de natalidade de 3%
# ano. Sabe-se que, atualmente, o país A tem população maior que o país B. Faça um programa que leia a
# população de cada país e imprima o tempo necessário para que a população do país B ultrapasse a
# população do país A.

# Define a função para calcular o tempo necessário para que a população B ultrapasse a população A.
def tempo_para_ultrapassar(populacao_A, populacao_B):
    # Define as taxas de natalidade para A e B.
    taxa_natalidade_A = 2 / 100
    taxa_natalidade_B = 3 / 100

    # Inicializa o contador de anos.
    anos = 0

    # Loop continua até que a população B ultrapasse a população A.
    while populacao_B <= populacao_A:
        # Atualiza as populações com base nas taxas de natalidade.
        populacao_A *= (1 + taxa_natalidade_A)
        populacao_B *= (1 + taxa_natalidade_B)

        # Incrementa o contador de anos.
        anos += 1

    # Retorna o número de anos necessário.
    return anos


def main():
    # Solicita a população do país A ao usuário.
    populacao_A = int(input("Digite a população do país A: ").strip())
    # Solicita a população do país B ao usuário.
    populacao_B = int(input("Digite a população do país B: ").strip())

    # Chama a função para calcular o tempo necessário.
    anos_necessarios1 = tempo_para_ultrapassar(populacao_A, populacao_B)
    anos_necessarios2 = tempo_para_ultrapassar(populacao_B, populacao_A)

    # Imprime o resultado para o usuário.
    print(f"O tempo necessário para que a população do país B ultrapasse a população do país A é de: {max(anos_necessarios1, anos_necessarios2)} anos!")


if __name__ == '__main__':
    main()
