# 02. Nem sempre as transações financeiras resultam em números inteiros. Vamos usar o round() para resolver isso!
# Peça ao usuário para inserir uma quantidade de dinheiro. Em seguida, arredonde esse valor para o número inteiro
# mais próximo e imprima o resultado.

# Esta função recebe um valor como argumento e utiliza a função 'round()' para arredondá-lo
def arredonda(valor):
    return round(valor)


# Essa função é o programa principal
def main():
    # Usa 'input()' para obter um número decimal do usuário. Em seguida, chama a função 'arredonda()' com o número
    # fornecido como argumento e imprime o resultado
    print(f"\n-> VALOR ARREDONDADO: {arredonda(float(input('Digite um número real qualquer: ').strip()))}")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
