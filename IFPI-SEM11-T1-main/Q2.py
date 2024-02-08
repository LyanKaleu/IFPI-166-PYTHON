# 02. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
# número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos
# (excluindo o zero).

# Define uma função chamada 'num'.
def num():
    # Inicializa as variáveis 'soma' e 'quantidade' com 0.
    soma = quantidade = 0

    # Inicia um loop while.
    while True:
        # Solicita ao usuário que digite um número inteiro positivo.
        n = int(input('-> Digite um número inteiro positivo qualquer (digite 0 para encerrar): '))

        # Verifica se o número digitado é igual a 0.
        if n == 0:
            # Se for, encerra o loop.
            break

        # Verifica se o número digitado é maior que 0.
        if n > 0:
            # Se for, adiciona o número à soma e incrementa a quantidade de números lidos.
            soma += n
            quantidade += 1

    # Verifica se pelo menos um número positivo foi digitado.
    if quantidade > 0:
        # Calcula a média aritmética e a imprime na tela.
        media = soma / quantidade
        print(f"\n-> A MÉDIA ARITMÉTICA DE TODOS OS NÚMEROS LIDOS: {media:.2f}")


# Define a função principal chamada 'main'.
def main():
    # Chama a função 'num' para iniciar a execução do programa.
    num()


# Verifica se este script está sendo executado diretamente.
if __name__ == '__main__':
    # Se sim, chama a função 'main'.
    main()
