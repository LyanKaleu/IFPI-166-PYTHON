def horas_e_minutos(minutos):
    h = minutos // 60
    m = minutos % 60
    return h, m


def main():
    min = int(input("Digite a quantidade de minutos: "))

    horas, minutos = horas_e_minutos(min)
    print("\nCONVERSÃO DE MINUTOS PARA HORAS E MINUTOS")
    print(f"-> {horas}h{minutos}min")


if __name__ == '__main__':
    main()
