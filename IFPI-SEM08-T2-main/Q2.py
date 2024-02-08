# 02. Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos se o valor lido for entre 0 (zero) e
# 100 mil ou -1 (menos um) para outros valores. Exemplo: 12.476 deve mostrar a 20.

# Define uma função chamada soma_digitos que recebe um argumento chamado numero
def soma_digitos(numero):
    # Inicializa uma variável soma para guardar a soma dos dígitos
    soma = 0

    # Verifica se o número está no intervalo [0, 100000)
    if 0 <= numero < 100000:
        # Para cada dígito do número (no máximo 5 dígitos), faz o seguinte:
        # Extrai o dígito da unidade e soma à variável soma
        digito_1 = numero % 10
        soma += digito_1
        # Remove o dígito da unidade, movendo para a direita
        numero //= 10

        # Repete os passos anteriores para os próximos dígitos
        digito_2 = numero % 10
        soma += digito_2
        numero //= 10

        digito_3 = numero % 10
        soma += digito_3
        numero //= 10

        digito_4 = numero % 10
        soma += digito_4
        numero //= 10

        digito_5 = numero % 10
        soma += digito_5

        # Retorna a soma dos dígitos
        return soma
    else:
        # Se o número não está no intervalo válido, retorna -1
        return -1


# Função principal do programa
def main():
    # Lê um número inteiro do usuário e remove espaços em branco
    n = int(input("Digite um número inteiro qualquer: ").strip())

    # Chama a função soma_digitos e guarda o resultado
    resultado = soma_digitos(n)

    # Imprime o resultado
    print(f"\n-> Soma dos dígitos do número informado: {resultado} dígitos!")


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Chama a função principal
    main()
