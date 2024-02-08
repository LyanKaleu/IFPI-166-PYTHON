# 5. Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa
# deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
# IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e
# retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso.

def ler_lista(n):
    lista = []
    print("Digite os valores da lista:")
    for i in range(n):
        lista.append(input().strip())  # Lê e adiciona cada valor à lista

    return lista


def esta_ordenado(lista):
    for i in range(len(lista) - 1):  # Percorre a lista até o penúltimo elemento
        if lista[i] > lista[i + 1]:  # Verifica se o elemento atual é maior que o próximo
            return False  # Se sim, a lista não está ordenada
    return True  # Se não houver violação, a lista está ordenada


def main():
    n = int(input('Informe o tamanho da lista: ').strip())  # Lê a quantidade de elementos da lista

    lista = ler_lista(n)  # Chama a função para ler a lista de valores

    if esta_ordenado(lista):  # Verifica se a lista está ordenada
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")


if __name__ == '__main__':
    main()  # Chama a função principal
