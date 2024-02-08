# 2. Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe
# uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo
# count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2
# aparece na lista.
# Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois
# o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.

def contagem(lista, valor):
    contador = 0
    for elemento in lista:
        if elemento == valor:
            contador += 1
    return contador


def main():
    # Leitura dos valores para a lista
    lista = []
    while True:
        entrada = int(input("Digite um número para a lista (0 para encerrar): ").strip())
        if entrada == 0:
            break
        lista.append(entrada)

    # Valor a ser pesquisado na lista
    valor_pesquisado = int(input("Digite o valor a ser pesquisado na lista: ").strip())

    # Resultado
    resultado = contagem(lista, valor_pesquisado)
    print(f"\n-> Lista lida: {lista}")
    print(f"-> Valor pesquisado: {valor_pesquisado}")
    print(f"-> Quantidade de vezes que o valor aparece na lista: {resultado}")


if __name__ == '__main__':
    main()
