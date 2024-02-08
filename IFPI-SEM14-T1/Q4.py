# 4. Um time de basquete possui 12 jogadores. Deseja-se um programa que, dado o nome e a altura
# dos jogadores, determine:
# a. o nome e a altura do jogador mais alto;
# b. a média de altura do time;
# c. os jogadores com altura superior à média, listando o nome e a altura de cada um.

def jogador_mais_alto(jogadores):
    mais_alto = jogadores[0]
    for jogador in jogadores[1:]:
        if jogador[1] > mais_alto[1]:
            mais_alto = jogador
    return mais_alto


def media_altura(jogadores):
    total_altura = 0
    for jogador in jogadores:
        total_altura += jogador[1]
    return total_altura / len(jogadores)


def acima_da_media(jogadores, media):
    acima_media = []
    for jogador in jogadores:
        if jogador[1] > media:
            acima_media.append(jogador)
    return acima_media


def main():
    # Inicializa a lista de jogadores
    jogadores = []
    n = 12  # Número de jogadores

    for indice in range(n):
        nome = input(f"Digite o nome do jogador {indice + 1}: ").strip()
        altura = float(input(f"Digite a altura do jogador {indice + 1} em centímetros: ").strip())
        jogadores.append([nome, altura])

    # a. Encontrar o jogador mais alto
    mais_alto = jogador_mais_alto(jogadores)
    print("\nJOGADOR MAIS ALTO DO TIME")
    print(f"-> O jogador mais alto é {mais_alto[0]} com {mais_alto[1]} cm de altura.\n")

    # b. Calcular a média de altura do time
    media = media_altura(jogadores)
    print("\nALTURA MÉDIA DO TIME")
    print(f"-> A média de altura do time é {media:.2f} cm.\n")

    # c. Jogadores com altura acima da média
    acima_media = acima_da_media(jogadores, media)
    print("\nJOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for jogador in acima_media:
        print(f"-> Nome: {jogador[0]}, Altura: {jogador[1]} cm")


if __name__ == '__main__':
    main()

