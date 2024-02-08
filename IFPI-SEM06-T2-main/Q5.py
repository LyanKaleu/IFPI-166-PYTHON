# 05. Você sabia que os pinguins usam jaquetas devido ao frio na Antártida? Vamos ajudá-los a converter temperaturas!
# Escreva um programa que leia uma temperatura em Celsius e mostre o resultado em Fahrenheit. Lembre-se:
# °F = (°C * (9/5)) + 32

# A função recebe a temperatura em graus Celsius como entrada
def converter_temperatura(celsius):

    # Converte a temperatura para Fahrenheit usando a fórmula: °F = (°C * (9/5)) + 32
    fahrenheit = (celsius * (9 / 5)) + 32

    # Retorna o valor em Fahrenheit
    return fahrenheit


# Essa função é o programa principal
def main():

    # Pede ao usuário que insira uma temperatura em graus Celsius, chamando a função 'converter_temperatura()' com a
    # temperatura inserida como argumento
    fahrenheit = converter_temperatura(float(input("Insira a temperatura em °C: ").strip()))

    # Imprime a temperatura em Fahrenheit na tela
    print(f"\n\n-> TEMPERATURA EM FAHRENHEIT: {fahrenheit:.2f}°F")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
