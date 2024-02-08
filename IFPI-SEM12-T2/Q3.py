# 03. Sendo H = 1 + 1/2 + 1/3 + 1;4 + ... + 1/n, escreva um programa para calcular o valor de H. O número n é lido.

def calcular_H(numero):
    soma = 0

    for i in range(1, numero + 1):
        termo = 1 / i
        soma += termo
    return soma


def main():
    n = int(input('Digite o valor de n: ').strip())
    resultado = calcular_H(n)
    print(f"O valor de H com n = {n} é aproximadamente {resultado:.4f}")


if __name__ == '__main__':
    main()
