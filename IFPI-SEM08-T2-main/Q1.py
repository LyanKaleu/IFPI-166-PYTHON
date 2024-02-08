# 01. Escreva um programa que leia um número inteiro e some 5 caso valor lido seja par ou some 8 caso o valor lido seja
# ímpar. Mostre na tela o resultado da operação.

# Define uma função chamada soma_5_par que recebe um argumento chamado numero
def soma_5_par(numero):
    # Verifica se o número é par (resto da divisão por 2 é 0)
    if numero % 2 == 0:
        # Se for par, adiciona 5 ao número
        numero += 5
    # Retorna o número modificado ou não, dependendo se era par ou não
    return numero


# Define uma função chamada soma_8_impar que recebe um argumento chamado numero
def soma_8_impar(numero):
    # Verifica se o número é ímpar (resto da divisão por 2 é diferente de 0)
    if numero % 2 != 0:
        # Se for ímpar, adiciona 8 ao número
        numero += 8
    # Retorna o número modificado ou não, dependendo se era ímpar ou não
    return numero


# Define a função principal do programa
def main():
    # Lê um número inteiro do usuário e remove espaços em branco
    n = int(input("Digite um número inteiro qualquer: ").strip())

    # Verifica se o número lido é par ou ímpar
    if n % 2 == 0:
        # Se for par, chama a função soma_5_par e imprime o resultado
        print(f"\nO número informado é par, então:\n{n} + 5 = {soma_5_par(n)}")
    else:
        # Se for ímpar, chama a função soma_8_impar e imprime o resultado
        print(f"\nO número informado é ímpar, então:\n{n} + 8 = {soma_8_impar(n)}")


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Chama a função principal
    main()
