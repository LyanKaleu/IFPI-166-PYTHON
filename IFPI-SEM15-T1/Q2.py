# Esta função recebe duas temperaturas com escalas diferentes e retorna a soma delas em uma escala comum.
def soma_temperaturas(t1, t2):
    # Verifica se as escalas das temperaturas são iguais.
    if t1[1] == t2[1]:
        # Se as escalas são iguais, soma os valores das temperaturas diretamente.
        resultado = round(t1[0] + t2[0], 4)
        return resultado, t1[1]  # Retorna a tupla com o resultado da soma e a escala de t1
    else:
        # Se as escalas são diferentes, converte a temperatura t1 para a escala da temperatura t2 e realiza a soma.
        if t2[1] == 'C':  # Se a segunda temperatura estiver em Celsius,
            conversao = (t1[0] - 32) * (5 / 9)  # converte a primeira temperatura para Celsius.
            resultado = round(conversao + t2[0], 4)  # Soma as temperaturas e arredonda o resultado.
            return resultado, 'C'  # Retorna a tupla com o resultado da soma e a escala Celsius
        else:  # Se a segunda temperatura estiver em Fahrenheit,
            conversao = (t1[0] * (9 / 5)) + 32  # converte a primeira temperatura para Fahrenheit.
            resultado = round(conversao + t2[0], 4)  # Soma as temperaturas e arredonda o resultado.
            return resultado, 'F'  # Retorna a tupla com o resultado da soma e a escala Fahrenheit


def main():
    # Solicita ao usuário o valor e a escala da primeira temperatura.
    valor1 = float(input("Digite o valor da primeira temperatura: ").strip())
    escala1 = input("Digite a escala da primeira temperatura (C para Celsius ou F para Fahrenheit): ").upper()[0]
    t1 = (valor1, escala1)  # Cria uma tupla com o valor e a escala da primeira temperatura.

    # Solicita ao usuário o valor e a escala da segunda temperatura.
    valor2 = float(input("\nDigite o valor da segunda temperatura: ").strip())
    escala2 = input("Digite a escala da segunda temperatura (C para Celsius ou F para Fahrenheit): ").upper()[0]
    t2 = (valor2, escala2)  # Cria uma tupla com o valor e a escala da segunda temperatura.

    # Exibe a soma das temperaturas inseridas pelo usuário.
    print("\nA soma das temperaturas é:", soma_temperaturas(t1, t2))


if __name__ == '__main__':
    main()
