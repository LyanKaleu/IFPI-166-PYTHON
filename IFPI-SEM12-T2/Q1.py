# 01. Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
# N ! = 1 x 2 x 3 x ... x N-1 x N
# 0 ! = 1

def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


def main():
    num = int(input('Digite um número inteiro qualquer: ').strip())

    if num < 0:
        print("O fatorial não está definido para números negativos.")
    else:
        resultado = calcular_fatorial(num)
        print(f"O fatorial de {num} é: {resultado}")


if __name__ == '__main__':
    main()
