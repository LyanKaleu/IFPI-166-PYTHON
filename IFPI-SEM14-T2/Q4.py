# 4. Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o
# produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto
# escalar, sendo que o produto escalar e dado por: (x1 ∗ y1) + (x2 ∗ y2) + (x3 ∗ y3) + ⋯ + (xn ∗ yn).

# Função para ler uma lista de 5 números reais digitados pelo usuário
def ler_lista():
    lista = []
    print("Digite 5 números reais:")
    for i in range(5):
        num = float(input().strip())
        lista.append(int(num))  # Armazena os números inteiros na lista
    return lista


# Função para calcular o produto escalar entre duas listas
def produto_escalar(lista_x, lista_y):
    resultado = 0
    formula = ''
    for indice in range(5):
        # Cria a representação da fórmula do produto escalar
        if indice != 4:
            formula += f"({lista_x[indice]} x {lista_y[indice]}) + "
        else:
            formula += f"({lista_x[indice]} x {lista_y[indice]}) = "

        # Calcula o produto escalar
        produto = lista_x[indice] * lista_y[indice]
        resultado += produto

    return f"{formula}{resultado}"  # Retorna a fórmula e o resultado do produto escalar


# Função principal que lê duas listas e calcula o produto escalar entre elas
def main():
    print("CONJUNTO X")
    lista_x = ler_lista()  # Chama a função para ler a primeira lista
    print("\nCONJUNTO Y")
    lista_y = ler_lista()  # Chama a função para ler a segunda lista

    print(f"\n-> Conjunto X: {lista_x}")  # Imprime a lista X
    print(f"-> Conjunto Y: {lista_y}")  # Imprime a lista Y
    print(f"-> Produto escalar: {produto_escalar(lista_x, lista_y)}")  # Calcula e imprime o produto escalar


if __name__ == '__main__':
    main()
