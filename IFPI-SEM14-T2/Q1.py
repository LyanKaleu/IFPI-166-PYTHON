# 1. Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior
# elemento e a posição que ele se encontra.

# Função para ler a lista de 10 números inteiros digitados pelo usuário
def ler_lista():
    lista = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        num = int(input().strip())
        lista.append(num)
    return lista


# Função para encontrar o maior elemento na lista e sua posição
def maior_elemento(lista):
    maior = max(lista)  # Encontra o maior número na lista
    posicao = lista.index(maior)  # Encontra a posição do maior número na lista
    return f"-> Lista: {lista}\n-> Maior elemento: {maior}\n-> Posição do maior elemento: {posicao}"


# Função principal que chama as outras funções e imprime os resultados
def main():
    lista = ler_lista()  # Chama a função para ler a lista
    resultado = maior_elemento(lista)  # Chama a função para encontrar o maior elemento
    print(resultado)  # Imprime a lista, o maior elemento e sua posição


if __name__ == '__main__':
    main()
