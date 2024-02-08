# 1. Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura
# de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista
# onde cada valor da lista original é a multiplicado pelo valor da constante.
# IMPORTANTE: Crie uma função chamada multiplica_constante() que receba a lista original e
# o valor da constante e retorna uma nova lista com os elementos multiplicados.

def ler_lista():
    lista = []
    while True:
        n = int(input("Digite um número inteiro (0 para encerrar): ").strip())  # Solicita um número inteiro ao usuário
        if n == 0:
            break  # Se o número for zero, encerra a leitura da lista
        else:
            lista.append(n)  # Adiciona o número à lista
        
    return lista  # Retorna a lista preenchida com os números fornecidos pelo usuário


def multiplica_constante(lista_original, constante):
    lista_nova = []
    for i in range(len(lista_original)):
        lista_nova.append(lista_original[i] * constante)  # Multiplica cada elemento da lista pela constante

    return lista_nova  # Retorna a nova lista com os elementos multiplicados pela constante


def main():
    print("Digite uma sequência de números inteiros:")
    lista_original = ler_lista()  # Chama a função para preencher a lista com números inteiros

    const = int(input("Digite um valor inteiro para definir a constante: ").strip())  # Solicita um valor inteiro constante ao usuário

    resultado = multiplica_constante(lista_original, const)  # Multiplica os elementos da lista pela constante
    print("Lista multiplicada pelo valor constante:", resultado)  # Imprime a nova lista com os valores multiplicados


if __name__ == '__main__':
    main()  # Chama a função principal
