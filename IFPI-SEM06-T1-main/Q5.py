# 05. Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à vista, vender pelo
# preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar em 10 vezes. Escreva um programa que
# leia o valor de uma compra e imprima três valores, todos com até duas casas decimais: • Valor para pagamento à
# vista, com desconto de 9%. • Valor da prestação para pagamento em 5 vezes, sem desconto nem juros. • Valor da
# prestação para pagamento em 10 vezes, com 17% de juros.

# Esta função recebe o valor total da compra como entrada e retorna três valores calculados a seguir:
def calcular_pagamento(valor_compra):
    # Calcula o valor com desconto para pagamento à vista
    valor_vista = valor_compra * 0.91  # 9% de desconto

    # Calcula o valor das prestações para pagamento em 5 vezes
    valor_prestacao_5x = valor_compra / 5

    # Calcula o valor das prestações para pagamento em 10 vezes com juros
    valor_prestacao_10x = valor_compra * 1.17 / 10  # 17% de juros

    return round(valor_vista, 2), round(valor_prestacao_5x, 2), round(valor_prestacao_10x, 2)


# Essa função é o programa principal
def main():
    # Lê o valor da compra do usuário
    valor_compra = float(input("Digite o valor da compra: ").strip())

    # Chama a função para calcular os valores
    vista, prestacao_5x, prestacao_10x = calcular_pagamento(valor_compra)

    # Imprime os resultados
    print(f"Valor à vista (com desconto de 9%): R$ {vista}")
    print(f"Valor da prestação em 5 vezes: R$ {prestacao_5x}")
    print(f"Valor da prestação em 10 vezes (com 17% de juros): R$ {prestacao_10x}")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
