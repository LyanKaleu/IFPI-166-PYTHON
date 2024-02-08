# Função para ler uma matriz de tamanho n x m a partir de entradas do usuário.
def ler_matriz(n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            elemento = int(input(
                f"Digite o elemento da posição ({i + 1}, {j + 1}): "))  # Solicita ao usuário o valor do elemento da matriz.
            linha.append(elemento)  # Adiciona o elemento à linha.
        matriz.append(linha)  # Adiciona a linha à matriz.
    return matriz  # Retorna a matriz preenchida.


# Função para calcular várias estatísticas com base na matriz fornecida.
def calcular_resposta(matriz):
    # Calcula a soma dos elementos da primeira linha.
    soma_primeira_linha = sum(matriz[0])

    # Calcula a soma dos elementos da última coluna.
    soma_ultima_coluna = sum(linha[-1] for linha in matriz)

    # Calcula o total de elementos na matriz.
    total_elementos = sum(sum(linha) for linha in matriz)

    # Calcula a quantidade total de elementos na matriz.
    qtd_elementos = sum(len(linha) for linha in matriz)

    # Calcula a média dos elementos da matriz.
    media_elementos = total_elementos / qtd_elementos

    # Encontra o menor elemento na matriz.
    menor_elemento = min(min(linha) for linha in matriz)

    # Encontra o maior elemento na matriz.
    maior_elemento = max(max(linha) for linha in matriz)

    # Retorna os resultados calculados.
    return soma_primeira_linha, soma_ultima_coluna, round(media_elementos, 4), menor_elemento, maior_elemento


def main():
    n = int(input("Digite o número de linhas da matriz: "))  # Solicita ao usuário o número de linhas da matriz.
    m = int(input("Digite o número de colunas da matriz: "))  # Solicita ao usuário o número de colunas da matriz.

    matriz = ler_matriz(n, m)  # Chama a função para ler a matriz.
    resposta = calcular_resposta(matriz)  # Calcula as estatísticas com base na matriz fornecida.

    # Imprime os resultados calculados.
    print(f"\n-> Soma dos elementos da primeira linha: {resposta[0]}")
    print(f"-> Soma dos elementos da última coluna: {resposta[1]}")
    print(f"-> Média dos elementos da matriz: {resposta[2]}")
    print(f"-> Menor elemento da matriz: {resposta[3]}")
    print(f"-> Maior elemento da matriz: {resposta[4]}")


if __name__ == '__main__':
    main()  # Chama a função principal.
