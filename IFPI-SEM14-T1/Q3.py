# 3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo
# tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.

def ler_lista():
    lista = []
    for i in range(20):
        elemento = int(input().strip())  # Solicita um número inteiro ao usuário
        lista.append(elemento)  # Adiciona o número à lista

    return lista  # Retorna a lista preenchida com os números fornecidos pelo usuário


def somar_listas(lista_a, lista_b):
    lista_c = []
    for indice in range(len(lista_a)):
        soma = lista_a[indice] + lista_b[indice]
        lista_c.append(soma)
    return lista_c


def main():
    # Leitura das listas A e B
    print("Insira os valores para a lista A:")
    lista_a = ler_lista()
    print("Insira os valores para a lista B:")
    lista_b = ler_lista()

    # Chamada da função para somar as listas A e B
    lista_c = somar_listas(lista_a, lista_b)

    # Exibição da lista resultante
    print("\n-> Lista A:", lista_a)
    print("-> Lista B:", lista_b)
    print("-> Lista C (Soma de A e B):", lista_c)


if __name__ == '__main__':
    main()
