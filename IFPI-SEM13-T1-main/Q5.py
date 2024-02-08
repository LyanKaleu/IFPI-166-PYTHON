# 5. Leia duas listas A e B contendo 25 elementos inteiros cada, gerar e imprimir uma lista C de 50 elementos,
# cujos elementos sejam a intercalação dos elementos de A e B.

def ler_lista():
    lista = []
    for i in range(25):
        elemento = int(input(f"Insira o {i+1}º número inteiro: ").strip())  # Solicita um número inteiro ao usuário
        lista.append(elemento)  # Adiciona o número à lista

    return lista  # Retorna a lista preenchida com os números fornecidos pelo usuário


def intercalar_listas(lista_a, lista_b):
    lista_c = []
    for i in range(25):
        lista_c.append(lista_a[i])  # Adiciona o elemento da lista A à lista C
        lista_c.append(lista_b[i])  # Adiciona o elemento da lista B à lista C

    return lista_c  # Retorna a lista C com os elementos intercalados de A e B


def main():
    print("Insira os elementos da lista A:")  # Mensagem indicando que o usuário deve inserir os elementos da lista A
    lista_a = ler_lista()  # Chama a função para preencher a lista A com 25 elementos

    print("Insira os elementos da lista B:")  # Mensagem indicando que o usuário deve inserir os elementos da lista B
    lista_b = ler_lista()  # Chama a função para preencher a lista B com 25 elementos

    lista_c = intercalar_listas(lista_a, lista_b)  # Intercala os elementos das listas A e B na lista C
    print("Lista A:", lista_a)  # Imprime a lista A
    print("Lista B:", lista_b)  # Imprime a lista B
    print("Lista C (intercalada):", lista_c)  # Imprime a lista C resultante da intercalação


if __name__ == '__main__':
    main()  # Chama a função principal
