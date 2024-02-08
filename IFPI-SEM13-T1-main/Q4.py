# 4. Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os números
# ímpares na lista IMPAR. Imprima as três listas.

def ler_lista():
    lista = []
    for i in range(20):
        lista.append(int(input(f"Insira o {i+1}º número inteiro: ").strip()))  # Solicita ao usuário que digite um número inteiro

    return lista  # Retorna a lista com os números inseridos pelo usuário


def lista_par(lista):
    PAR = []
    for i in range(20):
        if lista[i] % 2 == 0:
            PAR.append(lista[i])  # Adiciona números pares à lista PAR

    return PAR  # Retorna a lista PAR com os números pares


def lista_impar(lista):
    IMPAR = []
    for i in range(20):
        if lista[i] % 2 != 0:
            IMPAR.append(lista[i])  # Adiciona números ímpares à lista IMPAR

    return IMPAR  # Retorna a lista IMPAR com os números ímpares


def main():
    numeros = ler_lista()
    print("Números inseridos:", numeros)  # Imprime os números inseridos pelo usuário
    print("Números pares:", lista_par(numeros))  # Imprime os números pares da lista
    print("Números ímpares:", lista_impar(numeros))  # Imprime os números ímpares da lista


if __name__ == '__main__':
    main()  # Chama a função principal
