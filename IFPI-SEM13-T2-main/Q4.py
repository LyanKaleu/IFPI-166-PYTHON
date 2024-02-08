# 4. Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
# um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos
# anteriores da lista original.
# IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna
# uma lista com a soma cumulativa.

def ler_lista():
    lista = []
    print("Digite os números (digite 0 para encerrar):")
    while True:
        n = int(input().strip())  # Lê um número inteiro fornecido pelo usuário
        if n == 0:
            break  # Encerra a leitura quando o usuário insere 0
        else:
            lista.append(n)  # Adiciona o número à lista

    return lista


def soma_cumulativa(lista):
    for i in range(1, len(lista)):  # Começa do segundo elemento da lista
        lista[i] += lista[i-1]  # Soma o elemento atual com o elemento anterior

    return lista


def main():
    lista_original = ler_lista()  # Chama a função para ler a lista de números
    resultado = soma_cumulativa(lista_original)  # Chama a função para calcular a soma cumulativa
    print("Lista com a soma cumulativa dos elementos anteriores:")
    print(resultado)  # Imprime a lista resultante com a soma cumulativa dos elementos


if __name__ == '__main__':
    main()  # Chama a função principal
