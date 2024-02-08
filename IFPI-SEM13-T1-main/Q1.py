# 1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.

def ler_lista():
    lista = []  # Cria uma lista vazia para armazenar os números
    for i in range(10):  # Loop para ler 10 números
        lista.append(int(input(f"Insira o {i+1}º número inteiro: ").strip()))  # Adiciona à lista cada número inteiro
        # digitado pelo usuário

    return lista  # Retorna a lista preenchida


def mostrar_lista(lista):
    print(f"A lista de números é: {lista}")  # Mostra a lista de números fornecida


def mostrar_soma_lista(lista):
    soma = 0  # Inicializa a variável para a soma
    for i in range(10):  # Loop para percorrer todos os números na lista
        soma += lista[i]  # Adiciona cada número à soma

    return soma  # Retorna o valor da soma


def mostrar_produto_lista(lista):
    produto = 1  # Inicializa a variável para o produto
    for i in range(10):  # Loop para percorrer todos os números na lista
        produto *= lista[i]  # Multiplica cada número pelo produto

    return produto  # Retorna o valor do produto


def main():
    lista = ler_lista()  # Chama a função para ler os números e armazená-los em 'lista'
    mostrar_lista(lista)  # Mostra os números fornecidos
    print(f"A soma dos números é: {mostrar_soma_lista(lista)}")  # Mostra a soma dos números
    print(f"O produto dos números é: {mostrar_produto_lista(lista)}")  # Mostra o produto dos números


if __name__ == '__main__':
    main()  # Chama a função principal
