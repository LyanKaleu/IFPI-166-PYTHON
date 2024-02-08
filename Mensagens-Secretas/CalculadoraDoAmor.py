def calcular_compatibilidade(nome1, nome2):
    palavra_amor = "amor"
    vogais = "aeiou"
    placar = 0
    min_len = min(len(nome1), len(nome2))

    for i in range(min_len):
        char1 = nome1[i].lower()
        char2 = nome2[i].lower()

        if char1 in palavra_amor:
            placar += 2
        if char2 in palavra_amor:
            placar += 2

        if char1 in vogais:
            placar += 1
        if char2 in vogais:
            placar += 1

    return placar


def main():
    nome1 = input("Digite o nome da primeira pessoa: ")
    nome2 = input("Digite o nome da segunda pessoa: ")

    placar = calcular_compatibilidade(nome1, nome2)

    if placar < 10:
        print(f"O placar de compatibilidade é {placar}. Esqueça esta pessoa! Nunca vai dar certo!")
    elif placar < 15:
        print(f"O placar de compatibilidade é {placar}. Vocês têm alguma afinidade!")
    else:
        print(f"O placar de compatibilidade é {placar}. Parece promissor!")


if __name__ == '__main__':
    main()
