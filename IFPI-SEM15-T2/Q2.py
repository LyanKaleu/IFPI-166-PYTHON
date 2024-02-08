# Função para converter a temperatura para Kelvin, dada uma temperatura e uma escala (Celsius ou Fahrenheit).
def converter_para_kelvin(temperatura, escala):
    if escala == 'C':  # Verifica se a escala é Celsius.
        conversao = temperatura + 273.15  # Converte Celsius para Kelvin.
        return round(conversao, 2)  # Retorna a temperatura convertida em Kelvin, arredondada para 2 casas decimais.
    elif escala == 'F':  # Verifica se a escala é Fahrenheit.
        conversao = (temperatura - 32) * (5 / 9) + 273.15  # Converte Fahrenheit para Celsius e depois para Kelvin.
        return round(conversao, 2)  # Retorna a temperatura convertida em Kelvin, arredondada para 2 casas decimais.
    else:
        return temperatura  # Se a escala não for 'C' ou 'F', retorna a temperatura original.


# Função para converter o número do mês para o nome do mês correspondente.
def converter_para_mes(mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    if 1 <= mes <= 12:  # Verifica se o número do mês está entre 1 e 12.
        return meses[mes - 1]  # Retorna o nome do mês correspondente à posição na lista 'meses'.
    else:
        return None  # Se o número do mês não estiver entre 1 e 12, retorna None.


def main():
    temperaturas = []  # Inicializa uma lista vazia para armazenar as temperaturas convertidas para Kelvin.
    for i in range(1, 13):  # Loop de 1 a 12 (representando os meses do ano).
        temperatura = float(input(f"Digite a temperatura para o mês {i}: ").strip())  # Solicita ao usuário a temperatura.
        escala = input(f"Digite a escala para a temperatura do mês {i} (C/F): ").strip()  # Solicita ao usuário a escala da temperatura.

        temperatura_kelvin = converter_para_kelvin(temperatura, escala)  # Converte a temperatura para Kelvin.
        temperaturas.append(temperatura_kelvin)  # Adiciona a temperatura convertida à lista 'temperaturas'.

    media_anual_kelvin = round(sum(temperaturas) / len(temperaturas), 2)  # Calcula a média anual das temperaturas em Kelvin.
    print("\nTEMPERATURA MÉDIA ANUAL")
    print(f"{media_anual_kelvin:g}K")  # Imprime a temperatura média anual em Kelvin.

    print("\nTEMPERATURAS ACIMA DA MÉDIA ANUAL:")
    for i in range(12):  # Loop para os 12 meses do ano.
        if temperaturas[i] > media_anual_kelvin:  # Verifica se a temperatura do mês está acima da média anual.
            mes = converter_para_mes(i + 1)  # Converte o número do mês para o nome do mês correspondente.
            if mes:
                print(f"{mes}: {temperaturas[i]:g}K")  # Imprime o nome do mês e a temperatura correspondente em Kelvin.


if __name__ == '__main__':
    main()  # Chama a função principal.
