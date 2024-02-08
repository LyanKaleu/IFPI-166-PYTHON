# 02. A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
# subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
# leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
# sempre será maior ou igual a 2.


def fibonacci(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "0, 1"
    else:
        sequencia_fibonacci = "0, 1"
        a, b = 0, 1
        for i in range(2, numero):
            proximo_termo = a + b
            sequencia_fibonacci += f", {proximo_termo}"
            a, b = b, proximo_termo
        return sequencia_fibonacci


def main():
    num = int(input(
        'Digite o valor de n primeiros termos da sequência de Fibonacci (maior ou igual a 2): ').strip())

    if num < 2:
        print("O valor de n deve ser maior ou igual a 2.")
    else:
        sequencia_fibonacci = fibonacci(num)
        print(
            f"A sequência de Fibonacci com os {num} primeiros termos é:\n{sequencia_fibonacci}")


if __name__ == '__main__':
    main()
