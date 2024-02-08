# 01. A tartaruga e a lebre vão apostar uma corrida. A lebre concede à tartaruga o direito de sair n sua frente.
# A tartaruga corre a 1 metro por minuto e a lebre corre a 10 metros por minuto. Faça um programa que
# leia quantos metros a tartaruga sai à frente da lebre e calcule quantos minutos levará até que a lebre alcance
# a tartaruga. Por exemplo, se a tartaruga sair 500 metros à frente a lebre alcança em 56 minutos.

def calcular_tempo(distancia_inicial):
    velocidade_lebre = 10
    velocidade_tartaruga = 1
    # Define a diferença de velocidade
    diferenca_de_velocidade = velocidade_lebre - velocidade_tartaruga  # Lebre corre a 10 m/min e tartaruga a 1 m/min
    # Inicializa o acumulador de tempo
    tempo_em_minutos = 0

    # Enquanto a distância for maior que zero
    while distancia_inicial > 0:
        # A lebre se aproxima da tartaruga a uma taxa de 9 metros por minuto
        distancia_inicial -= diferenca_de_velocidade
        # Incrementa o tempo em um minuto
        tempo_em_minutos += 1

    return tempo_em_minutos


def main():
    # Solicita a distância em metros pela qual a tartaruga está à frente da lebre
    dist_inicial = int(input('Informe a distância da tartaruga à frente da lebre (em metros): ').strip())
    tempo_em_minutos = calcular_tempo(dist_inicial)
    # Exibe o resultado
    print(f"A lebre alcançará a tartaruga em {tempo_em_minutos} minutos!")


if __name__ == '__main__':
    main()
