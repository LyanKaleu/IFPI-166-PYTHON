def calcular(a, b, c):
    return 2 * a + 5 * b - c


def main():
    print("Função: 2a + 5b - c")
    a = int(input("Digite o valor A: "))
    b = int(input("Digite o valor B: "))
    c = int(input("Digite o valor C: "))

    resultado = calcular(a, b, c)
    print(f"\n-> Resultado da função: {resultado}")


if __name__ == '__main__':
    main()
