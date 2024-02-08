# 01. Escreva um programa que pergunte o depósito inicial e a taxa de juros ao ano de uma poupança. Mostre
# em quantos anos o valor acumulado será o dobro do valor inicial. Por exemplo:
# R$100,00 rendendo 8% ao ano irá
# dobrar em 10 anos.
# Início R$ 100.00
# 1 ano R$ 108.00
# 2 anos R$ 116.64
# 3 anos R$ 125.97
# 4 anos R$ 136.05
# 5 anos R$ 146.93
# 6 anos R$ 158.69
# 7 anos R$ 171.38
# 8 anos R$ 185.09
# 9 anos R$ 199.90
# 10 anos R$ 215.89
#
# R$100,00 rendendo 10% ao ano
# irá dobrar em 8 anos.
# Início R$ 100.00
# 1 ano R$ 110.00
# 2 anos R$ 121.00
# 3 anos R$ 133.10
# 4 anos R$ 146.41
# 5 anos R$ 161.05
# 6 anos R$ 177.16
# 7 anos R$ 194.87
# 8 anos R$ 214.36
#
# R$200,00 rendendo 15% ao ano
# irá dobrar em 5 anos.
# Início R$ 100.00
# 1 ano R$ 230.00
# 2 anos R$ 264.50
# 3 anos R$ 304.17
# 4 anos R$ 349.80
# 5 anos R$ 402.27
#
# Dica: use repetição com teste no início

# Define uma função chamada calcular_anos_dobro que recebe dois argumentos: deposito_inicial e taxa_juros.
def calcular_anos_dobro(deposito_inicial, taxa_juros):
    # Inicializa a variável anos com 0.
    anos = 0

    # Inicializa a variável resultado com o valor do depósito inicial.
    resultado = deposito_inicial

    # Enquanto o resultado for menor que o dobro do depósito inicial, o loop continuará.
    while resultado < (2 * deposito_inicial):
        # Atualiza o resultado adicionando os juros ao valor atual.
        resultado += resultado * (taxa_juros / 100)
        # Incrementa o número de anos.
        anos += 1

    # Retorna o número de anos necessários para dobrar o depósito.
    return anos


# Define a função principal chamada main.
def main():
    # Solicita ao usuário o valor inicial do depósito e converte para float.
    inicial = float(input('-> Informe o seu depósito inicial: ').strip())

    # Solicita ao usuário a taxa de juros e converte para float.
    taxa = float(input('-> Informe a taxa de juros ao ano de uma poupança: ').strip())

    # Chama a função calcular_anos_dobro com os valores fornecidos e armazena o resultado em 'anos'.
    anos = calcular_anos_dobro(inicial, taxa)

    # Imprime o número de anos necessário para dobrar o depósito.
    print(f"\nO valor acumulado será o dobro do valor inicial em {anos} anos!")


# Verifica se este script está sendo executado diretamente.
if __name__ == '__main__':
    # Se sim, chama a função main para iniciar a execução do programa.
    main()
