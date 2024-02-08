# 2. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com 0 (zero) e imprima a lista;
# b) preencha com os números de 1 a n e imprima a lista;
# c) preencha com valores inteiros lidos pelo teclado e imprima a lista;
# d) preencha na ordem inversa com valores inteiros lidos pelo teclado e imprima a lista; dica: use insert
# para sempre incluir os elementos no início da lista;

def lista_0(n):
    lista = []
    for i in range(n):
        lista.append(0)  # Adiciona o número zero à lista 'n' vezes

    return lista  # Retorna a lista preenchida com zeros


def lista_1_a_n(n):
    lista = []
    for i in range(n):
        lista.append(i+1)  # Adiciona números de 1 a 'n' à lista

    return lista  # Retorna a lista preenchida com números de 1 a 'n'


def lista_valores_lidos(n):
    lista = []
    for i in range(n):
        lista.append(int(input("Digite um valor inteiro: ").strip()))  # Solicita que o usuário digite um valor
        # inteiro e adiciona o valor à lista

    return lista  # Retorna a lista preenchida com valores lidos pelo usuário


def lista_inversa(n):
    lista = []
    for i in range(n):
        lista.insert(0, int(input("Digite um valor inteiro para a lista inversa: ").strip()))  # Solicita que o
        # usuário digite um valor inteiro e insere o valor no início da lista (ordem inversa)

    return lista  # Retorna a lista preenchida na ordem inversa


def main():
    n = int(input("Digite o tamanho da lista: ").strip())  # Solicita que o usuário digite o tamanho da lista
    print("Lista preenchida com zeros:", lista_0(n))  # Mostra a lista preenchida com zeros
    print("Lista preenchida de 1 a", n, ":", lista_1_a_n(n))  # Mostra a lista preenchida com números de 1 a 'n'
    print("Preencha a lista com valores inteiros:")
    print("Lista preenchida com valores lidos:", lista_valores_lidos(n))  # Mostra a lista preenchida com valores lidos pelo usuário
    print("Lista preenchida na ordem inversa:", lista_inversa(n))  # Mostra a lista preenchida na ordem inversa


if __name__ == '__main__':
    main()  # Chama a função principal
