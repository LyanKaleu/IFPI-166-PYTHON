# Esta função compara duas temperaturas e determina qual é maior.
def determinar_temperatura_maior(t1, t2):
    conversao = 0

    # Verifica se as escalas são iguais.
    if t1[1] == t2[1]:
        # Se as escalas são iguais, compara os valores diretamente.
        if t1[0] > t2[0]:
            return t1  # Retorna a primeira temperatura se for maior.
        else:
            return t2  # Retorna a segunda temperatura se for maior.
    else:
        # Se as escalas são diferentes, é necessário fazer uma conversão para comparar.
        if t1[1] == 'C':  # Verifica se a primeira temperatura está em Celsius.
            # Converte a primeira temperatura de Celsius para Fahrenheit.
            conversao = (t1[0] * (9/5)) + 32
            # Compara a temperatura convertida com a segunda temperatura.
            if conversao > t2[0]:
                return t1  # Retorna a primeira temperatura se for maior após conversão.
            else:
                return t2  # Retorna a segunda temperatura se for maior após conversão.
        else:
            # Converte a primeira temperatura de Fahrenheit para Celsius.
            conversao = (t1[0] - 32) * (5/9)
            # Compara a temperatura convertida com a segunda temperatura.
            if conversao > t2[0]:
                return t1  # Retorna a primeira temperatura se for maior após conversão.
            else:
                return t2  # Retorna a segunda temperatura se for maior após conversão.


def main():
    # Solicita ao usuário o valor e a escala da primeira temperatura.
    valor1 = float(input("Digite o valor da primeira temperatura: ").strip())
    escala1 = input("Digite a escala da primeira temperatura (C para Celsius ou F para Fahrenheit): ").upper()[0]
    t1 = (valor1, escala1)  # Cria uma tupla com o valor e a escala da primeira temperatura.

    # Solicita ao usuário o valor e a escala da segunda temperatura.
    valor2 = float(input("\nDigite o valor da segunda temperatura: ").strip())
    escala2 = input("Digite a escala da segunda temperatura (C para Celsius ou F para Fahrenheit): ").upper()[0]
    t2 = (valor2, escala2)  # Cria uma tupla com o valor e a escala da segunda temperatura.

    # Exibe a temperatura maior entre as duas inseridas pelo usuário.
    print("\nA temperatura maior é:", determinar_temperatura_maior(t1, t2))


if __name__ == '__main__':
    main()
