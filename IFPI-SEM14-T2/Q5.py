# 5. Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas
# anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.

# Importando a função de remover elementos repetidos da questão 3 dessa lista (Q3)
from Q3 import remover_repetidos


# Função para ler uma lista de 10 números digitados pelo usuário
def ler_lista():
    lista = []
    print("Digite 10 números inteiros:")
    for i in range(10):
        num = int(input().strip())
        lista.append(num)  # Adiciona os números à lista
    return lista


# Função para unir duas listas e eliminar elementos repetidos
def uniao_listas(lista_a, lista_b):
    return lista_a + lista_b  # Concatena as duas listas


# Função principal que lê duas listas e cria a união entre elas
def main():
    print("LISTA A")
    lista_a = ler_lista()  # Chama a função para ler a primeira lista
    print("\nLISTA B")
    lista_b = ler_lista()  # Chama a função para ler a segunda lista

    lista_c = uniao_listas(lista_a, lista_b)  # Chama a função para unir as listas

    # Imprime a lista resultante após remover os elementos repetidos
    print(f"\n-> Lista resultante da união sem elementos repetidos: {remover_repetidos(lista_c)}")


if __name__ == '__main__':
    main()
