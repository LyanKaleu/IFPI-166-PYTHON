def calcular_area(lado):
    area = lado ** 2
    return area


def calcular_perimetro(lado):
    perimetro = 4 * lado
    return perimetro


def main():
    lado = float(input("Digite o lado de um quadrado: "))

    area = calcular_area(lado)
    perimetro = calcular_perimetro(lado)

    print(f"\n\n-> ÁREA DO QUADRADO: {area:10.4f}")
    print(f"-> PERÍMETRO DO QUADRADO: {perimetro:10.4f}")


if __name__ == "__main__":
    main()
