# 02. Você tem uma poupança de 10 mil reais, que rende 0,7% ao mês. Você deseja comprar um carro, mas o
# preço do carro sobe a taxa de 0,4% ao mês. Escreva um programa que leia o preço de um carro hoje e
# calcule em quantos meses, com o dinheiro dessa aplicação, você terá dinheiro suficiente para comprar o
# carro à vista.

def calcular_meses_para_comprar_carro(saldo_inicial, taxa_poupanca, preco_carro, taxa_carro):
    meses = 0
    saldo = saldo_inicial

    while saldo < preco_carro:
        meses += 1
        saldo *= (1 + taxa_poupanca)
        preco_carro *= (1 + taxa_carro)

    return meses


def main():
    saldo_inicial = 10000
    taxa_poupanca = 0.007
    preco_carro = float(input("Informe o preço do carro: ").strip())
    taxa_carro = 0.004

    meses_necessarios = calcular_meses_para_comprar_carro(saldo_inicial, taxa_poupanca, preco_carro, taxa_carro)
    print(f"Com o dinheiro da aplicação, você poderá comprar o carro à vista em {meses_necessarios} meses.")


if __name__ == '__main__':
    main()
