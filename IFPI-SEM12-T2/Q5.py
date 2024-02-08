# 05. Escreva um programa que leia dois valores inteiros (x e y) e mostre todos os números primos entre x e y.

from Q4 import verificar_primo


def encontrar_primos_entre(x, y):
    print(f"Números primos entre {x} e {y}:")
    for num in range(x, y + 1):
        if verificar_primo(num):
            print(num)


def main():
    x = int(input("Digite o valor de x: ").strip())
    y = int(input("Digite o valor de y: ").strip())

    encontrar_primos_entre(x, y)


if __name__ == '__main__':
    main()
