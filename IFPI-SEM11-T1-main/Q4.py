# 04. Escreva um programa que leia número inteiro qualquer e mostre na forma invertida. Por exemplo:
# Para o número lido -> A saída será:
# 123 -> 321
# 1895 -> 5981
# 14960 -> 6941
# 53698423 -> 32489635

# Define uma função chamada 'inverter_numero' que recebe um argumento 'numero'.
def inverter_numero(numero):
    # Inicializa uma variável 'numero_invertido' com 0.
    numero_invertido = 0

    # Enquanto 'numero' for maior que 0, executa o loop.
    while numero > 0:
        # Obtém o último dígito de 'numero'.
        digito = numero % 10

        # Atualiza 'numero_invertido' para incluir o novo dígito.
        numero_invertido = numero_invertido * 10 + digito

        # Remove o último dígito de 'numero'.
        numero //= 10

    # Retorna o número invertido.
    return numero_invertido


# Define a função principal chamada 'main'.
def main():
    # Solicita ao usuário que digite um número inteiro e o converte para int.
    n = int(input('-> Digite um número inteiro qualquer: ').strip())

    # Chama a função 'inverter_numero' com o número fornecido e armazena o resultado em 'resultado'.
    resultado = inverter_numero(n)

    # Imprime o resultado.
    print(f"\n-> NÚMERO NA FORMA INVERTIDA: {resultado}")


# Verifica se este script está sendo executado diretamente.
if __name__ == '__main__':
    # Se sim, chama a função 'main' para iniciar a execução do programa.
    main()
