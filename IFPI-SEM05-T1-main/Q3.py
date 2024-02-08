def percentual(valor, porcentagem):
    return valor * (porcentagem/100)


def main():
    v = float(input("Digite o preço: "))
    p = float(input("Digite o valor percentual: "))

    valor = percentual(v, p)
    valor_acrescido = v + valor
    desconto = v - valor
    print(f"\n\n-> PREÇO ACRESCIDO DO PERCENTUAL: {valor_acrescido:.2f}")
    print(f"-> PREÇO COM O DESCONTO PERCENTUAL: {desconto:.2f}")


if __name__ == '__main__':
    main()
