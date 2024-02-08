# 03. Escreva um programa que leia 5 números inteiros e escreva o maior e o menor deles. Considere que todos os valores
# são diferentes. NÃO use as funções embutidas min() e max().

# Define a função 'maior_menor' que encontra o maior e menor número entre cinco valores.
def maior_menor(num1, num2, num3, num4, num5):
    # Define as variáveis 'maior' e 'menor' inicialmente como o primeiro número.
    maior = menor = num1

    # Compara o segundo número com o 'maior' e o 'menor'.
    if num2 > maior:
        maior = num2
    else:
        if num2 < menor:
            menor = num2

    # Compara o terceiro número com o 'maior' e o 'menor'.
    if num3 > maior:
        maior = num3
    else:
        if num3 < menor:
            menor = num3

    # Compara o quarto número com o 'maior' e o 'menor'.
    if num4 > maior:
        maior = num4
    else:
        if num4 < menor:
            menor = num4

    # Compara o quinto número com o 'maior' e o 'menor'.
    if num5 > maior:
        maior = num5
    else:
        if num5 < menor:
            menor = num5

    # Retorna o maior e o menor número.
    return maior, menor


def main():
    # Solicita e lê cinco números do usuário.
    n1 = int(input("Digite o primeiro número: ").strip())
    n2 = int(input("Digite o segundo número: ").strip())
    n3 = int(input("Digite o terceiro número: ").strip())
    n4 = int(input("Digite o quarto número: ").strip())
    n5 = int(input("Por fim, digite o quinto número: ").strip())

    # Chama a função 'maior_menor' com os números lidos e armazena o resultado em 'maior' e 'menor'.
    maior, menor = maior_menor(n1, n2, n3, n4, n5)

    # Imprime o maior e o menor número.
    print(f"\n-> O maior número é: {maior}")
    print(f"-> O menor número é: {menor}")


# Executa a função 'main' quando o script é executado diretamente.
if __name__ == '__main__':
    main()
