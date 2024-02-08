# 03. Escreva um programa que leia um número inteiro positivo e escreva na tela:
# • FIZZ se o número é divisível por três;
# • BUZZ se o número é divisível por cinco;
# • FIZZBUZZ se o número é divisível por três e por cinco ao mesmo tempo.
# • O próprio número caso não seja divisível por três ou por cinco.

# Define uma função chamada divisivel_3_5 que recebe um argumento chamado numero
def divisivel_3_5(numero):
    # Verifica se o número é divisível por 3
    if numero % 3 == 0:
        # Se for divisível por 3, verifica se também é divisível por 5
        if numero % 5 == 0:
            # Se for divisível por ambos, retorna 'FIZZBUZZ'
            return 'FIZZBUZZ'
        else:
            # Se for divisível apenas por 3, retorna 'FIZZ'
            return 'FIZZ'
    else:
        # Se não for divisível por 3
        # Verifica se é divisível por 5
        if numero % 5 == 0:
            # Se for divisível apenas por 5, retorna 'BUZZ'
            return 'BUZZ'
        else:
            # Se não for divisível por nenhum dos dois, retorna o próprio número
            return numero


# Função principal do programa
def main():
    # Lê um número inteiro do usuário e remove espaços em branco
    n = int(input("Digite um número inteiro qualquer: ").strip())

    # Chama a função divisivel_3_5 e guarda o resultado
    resultado = divisivel_3_5(n)

    # Imprime o resultado
    print(f"\n-> {resultado}")


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Chama a função principal
    main()
