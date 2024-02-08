# 2. Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
# ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
# multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
# DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.

def ler_lista():
    lista = []
    print("Digite uma lista com 100 números inteiros:")
    for i in range(100):
        lista.append(int(input().strip()))  # Lê os 100 números inteiros fornecidos pelo usuário
    
    return lista


def ordenar_lista(lista):
    return sorted(lista)  # Ordena a lista fornecida


def multiplicar_indice(lista):
    nova_lista = []
    for i in range(100):
        if i % 2 == 0:
            lista[i] *= 3  # Multiplica por 3 se o índice for par
            nova_lista.append(lista[i])
        else:
            lista[i] *= 5  # Multiplica por 5 se o índice for ímpar
            nova_lista.append(lista[i])      

    return nova_lista  # Retorna a nova lista com os elementos de índices pares e ímpares multiplicados


def main():
    lista_original = ler_lista()  # Chama a função para preencher a lista com 100 números inteiros
    lista_ordenada = ordenar_lista(lista_original)  # Ordena a lista fornecida
    resultado = multiplicar_indice(lista_ordenada)  # Multiplica os elementos da lista pelos fatores correspondentes
    print("Lista com elementos de índice par multiplicados por 3 "
          "e de índice ímpar multiplicados por 5:", resultado)  # Imprime a nova lista com os elementos modificados


if __name__ == '__main__':
    main()  # Chama a função principal
