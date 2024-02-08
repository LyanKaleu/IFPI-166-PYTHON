# Função para ler uma matriz quadrada de ordem N, onde N é fornecido pelo usuário.
def ler_matriz_quadrada():
    n = int(input("Digite a ordem da matriz quadrada: ").strip())  # Solicita ao usuário a ordem da matriz.
    matriz = []  # Inicializa uma lista vazia para armazenar a matriz.
    for i in range(n):  # Percorre as linhas da matriz.
        linha = []  # Inicializa uma lista vazia para cada linha da matriz.
        for j in range(n):  # Percorre os elementos de cada linha.
            elemento = int(input(f"Digite o elemento da posição [{i}][{j}]: ").strip())  # Solicita ao usuário cada elemento da matriz.
            linha.append(elemento)  # Adiciona o elemento à linha.
        matriz.append(linha)  # Adiciona a linha à matriz.
    return matriz  # Retorna a matriz preenchida.


# Função para encontrar as posições do maior e do menor elemento em uma matriz quadrada.
def encontrar_maior_menor(matriz):
    n = len(matriz)  # Obtém a ordem da matriz.
    maior = menor = matriz[0][0]  # Inicializa as variáveis de maior e menor elemento com o primeiro elemento da matriz.
    pos_maior = pos_menor = (0, 0)  # Inicializa as posições do maior e do menor elemento como a posição (0, 0).

    for i in range(n):  # Percorre as linhas da matriz.
        for j in range(n):  # Percorre os elementos de cada linha.
            if matriz[i][j] > maior:  # Verifica se o elemento atual é maior que o atual maior elemento encontrado.
                maior = matriz[i][j]  # Atualiza o valor do maior elemento.
                pos_maior = (i, j)  # Atualiza a posição do maior elemento.
            if matriz[i][j] < menor:  # Verifica se o elemento atual é menor que o atual menor elemento encontrado.
                menor = matriz[i][j]  # Atualiza o valor do menor elemento.
                pos_menor = (i, j)  # Atualiza a posição do menor elemento.

    return pos_maior, pos_menor  # Retorna as posições do maior e do menor elemento.


# Função principal: lê a matriz e encontra as posições do maior e do menor elementos, em seguida, imprime as posições encontradas.
def main():
    matriz = ler_matriz_quadrada()  # Chama a função para ler a matriz.
    posicao_maior, posicao_menor = encontrar_maior_menor(matriz)  # Chama a função para encontrar as posições do maior e do menor elemento.

    print(f"\nPosição do maior elemento: {posicao_maior}")  # Imprime a posição do maior elemento.
    print(f"Posição do menor elemento: {posicao_menor}")  # Imprime a posição do menor elemento.


if __name__ == '__main__':
    main()  # Chama a função principal.
