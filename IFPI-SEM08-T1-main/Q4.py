# 04. Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a
# média. Considere duas casas decimais.

# Define a função 'calcular_media' que calcula a média de cinco números.
def calcular_media(num1, num2, num3, num4, num5):
    soma = num1 + num2 + num3 + num4 + num5
    media = soma / 5
    return media


def main():
    # Solicita e lê cinco números do usuário.
    n1 = int(input("Digite o primeiro número: ").strip())
    n2 = int(input("Digite o segundo número: ").strip())
    n3 = int(input("Digite o terceiro número: ").strip())
    n4 = int(input("Digite o quarto número: ").strip())
    n5 = int(input("Por fim, digite o quinto número: ").strip())

    # Chama a função 'calcular_media' com os números lidos e armazena o resultado em 'media'.
    media = calcular_media(n1, n2, n3, n4, n5)

    # Imprime a média calculada.
    print(f"\n-> A média é: {media:.1f}")

    print("\n\t\tNÚMEROS MAIORES QUE A MÉDIA:")

    # Verifica se cada número é maior que a média e imprime se for o caso.
    if n1 > media:
        print(f"-> {n1}")

    if n2 > media:
        print(f"-> {n2}")

    if n3 > media:
        print(f"-> {n3}")

    if n4 > media:
        print(f"-> {n4}")

    if n5 > media:
        print(f"-> {n5}")


# Executa a função 'main' quando o script é executado diretamente.
if __name__ == '__main__':
    main()
