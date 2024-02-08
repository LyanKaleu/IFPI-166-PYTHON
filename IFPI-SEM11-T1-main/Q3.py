# 03. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
# número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
# (excluindo o zero).

# Define uma função chamada 'determinar_maior_menor'.
def determinar_maior_menor():
    # Solicita ao usuário que digite um número inteiro e o converte para int.
    maior = menor = int(input('-> Digite um número inteiro positivo qualquer (digite 0 para encerrar): ').strip())

    # Inicia um loop while.
    while True:
        # Solicita ao usuário que digite um número inteiro e o converte para int.
        numero = int(input('-> Digite um número inteiro positivo qualquer (digite 0 para encerrar): ').strip())

        # Verifica se o número digitado é igual a 0.
        if numero == 0:
            # Se for, encerra o loop.
            break

        # Verifica se o número digitado é maior que o 'maior' atual.
        if numero > maior:
            # Se for, atualiza o 'maior'.
            maior = numero

        # Verifica se o número digitado é menor que o 'menor' atual.
        if numero < menor:
            # Se for, atualiza o 'menor'.
            menor = numero

    # Retorna uma mensagem com o maior e menor números lidos.
    return f"\n-> MAIOR NÚMERO LIDO: {maior}\n-> MENOR NÚMERO LIDO: {menor}"


# Define a função principal chamada 'main'.
def main():
    # Chama a função 'determinar_maior_menor' e armazena o resultado em 'resultado'.
    resultado = determinar_maior_menor()

    # Imprime o resultado.
    print(resultado)


# Verifica se este script está sendo executado diretamente.
if __name__ == '__main__':
    # Se sim, chama a função 'main'.
    main()
