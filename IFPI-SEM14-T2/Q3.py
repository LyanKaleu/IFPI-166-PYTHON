# 3. Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando
# elementos repetidos.

# Função para ler uma lista de 20 números inteiros digitados pelo usuário
def ler_lista():
    lista = []
    print("Digite 20 números inteiros:")
    for i in range(20):
        num = int(input().strip())
        lista.append(num)
    return lista


# Função para remover elementos repetidos da lista
def remover_repetidos(lista):
    lista_sem_repeticao = []
    for elemento in lista:
        if elemento not in lista_sem_repeticao:
            lista_sem_repeticao.append(elemento)
    return lista_sem_repeticao


# Função principal que chama as outras funções e imprime a lista sem elementos repetidos
def main():
    numeros = ler_lista()  # Chama a função para ler a lista
    lista_sem_repeticao = remover_repetidos(numeros)  # Chama a função para remover elementos repetidos
    print(f"\n-> Lista sem elementos repetidos: {lista_sem_repeticao}")  # Imprime a lista sem elementos repetidos


if __name__ == '__main__':
    main()
