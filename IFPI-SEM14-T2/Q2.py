# 2. Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de
# números negativos e a soma dos números positivos dessa lista.

# Função para ler a lista de 10 números reais digitados pelo usuário
def ler_lista():
    lista = []
    print("Digite 10 números reais:")
    for i in range(10):
        num = float(input().strip())
        lista.append(int(num))
    return lista


# Função para determinar a quantidade de números negativos na lista
def determinar_negativos(lista):
    cont_negativo = 0
    for elemento in lista:
        if elemento < 0:
            cont_negativo += 1
    return cont_negativo


# Função para calcular a soma dos números positivos na lista
def soma_positivos(lista):
    soma = 0
    for elemento in lista:
        if elemento > 0:
            soma += elemento
    return soma


# Função principal que chama as outras funções e imprime os resultados
def main():
    lista = ler_lista()  # Chama a função para ler a lista
    print(f"\n-> Lista: {lista}")

    # Chama a função para determinar a quantidade de números negativos
    qtd_negativos = determinar_negativos(lista)
    print(f"-> Quantidade de números negativos: {qtd_negativos}")

    # Chama a função para calcular a soma dos números positivos
    soma_positivo = soma_positivos(lista)
    print(f"-> Soma dos números positivos: {soma_positivo}")


if __name__ == '__main__':
    main()
