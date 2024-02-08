# 03. Você foi ao mercado mágico e, ao comprar 3 maçãs e 2 bananas, o caixa precisa da sua ajuda para calcular o total!
# Leia o preço de uma maçã e o preço de uma banana, calcule e imprima o total da sua compra.

# Esta função recebe dois preços ('preco1' e 'preco2') como argumentos e retorna o valor total da compra,
# calculado como 3 x preco1 + 2 x preco2
def calcular_compra(preco1, preco2):
    return 3 * preco1 + 2 * preco2


# Essa função é o programa principal
def main():
    # Usa 'input()' para obter o preço da maçã e o preço da banana do usuário
    preco_maca = float(input("Insere o preço da maçã: ").strip())
    preco_banana = float(input("Por fim, o preço da banana: ").strip())

    # Chama a função 'calcular_compra()' com os preços fornecidos como argumentos e imprime o valor total da compra
    print(f"\n\n-> VALOR TOTAL DA COMPRA: {calcular_compra(preco_maca, preco_banana):.2f}")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
