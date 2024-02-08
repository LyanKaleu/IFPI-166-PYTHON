def inverte_numero(numero):
    if 1000 <= numero <= 9999:
        numero_str = str(numero)
        numero_invertido = numero_str[::-1]
        numero_invertido = int(numero_invertido)
        return numero_invertido
    else:
        return False


def main():
    numero = int(input("Digite um número inteiro entre 1000 e 9999: "))
    numero_invertido = inverte_numero(numero)
    print(f"Número na ordem inversa: {numero_invertido}")


if __name__ == '__main__':
    main()
