# 1. As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
# estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
# a) len(), que recebe uma lista e retorna número de itens;
# b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
# c) min(),que recebe uma lista e retorna o menor valor
# d) max(), que recebe uma lista retorna o maior valor
# e) sum(), que recebe uma lista retorna a soma dos valores
# Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
# leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o
# resultado encontrado.
# Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(),
# minimo(), maximo(), soma().

def comprimento(lista):
    contador = 0
    for indice in lista:
        contador += 1
    return contador


def inverter(lista):
    lista_invertida = []
    for indice in range(comprimento(lista) - 1, -1, -1):
        lista_invertida.append(lista[indice])
    return lista_invertida


def minimo(lista):
    menor = lista[0]
    for item in lista[1:]:
        if item < menor:
            menor = item
    return menor


def maximo(lista):
    maior = lista[0]
    for item in lista[1:]:
        if item > maior:
            maior = item
    return maior


def soma(lista):
    total = 0
    for item in lista:
        total += item
    return total


def main():
    # Leitura dos valores para a lista
    lista = []
    while True:
        valor = int(input("Digite um número (0 para encerrar): ").strip())
        if valor == 0:
            break
        lista.append(valor)

    # Resultados
    print(f"\n-> Lista lida: {lista}")
    print(f"-> Comprimento da lista: {comprimento(lista)}")
    print(f"-> Lista invertida: {inverter(lista)}")
    print(f"-> Menor valor da lista: {minimo(lista)}")
    print(f"-> Maior valor da lista: {maximo(lista)}")
    print(f"-> Soma dos valores da lista: {soma(lista)}")


if __name__ == '__main__':
    main()
