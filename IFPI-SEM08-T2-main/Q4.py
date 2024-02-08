# 04. Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para ‘homens’ e 2 para ‘mulheres’.
# Considerando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes fórmulas:
# • para homens: (72.7 * altura) – 58
# • para mulheres: (62.1 * altura) – 44.7

# Definindo uma função chamada peso_ideal que recebe dois argumentos: altura e sexo
def peso_ideal(altura, sexo):
    # Verifica se o sexo é masculino (1)
    if sexo == 1:
        # Fórmula para calcular o peso ideal para homens
        return (72.7 * altura) - 58
    else:
        # Se o sexo não é masculino, verifica se é feminino (2)
        if sexo == 2:
            # Fórmula para calcular o peso ideal para mulheres
            return (62.1 * altura) - 44.7


# Função principal do programa
def main():
    # Lê a altura do usuário como um número de ponto flutuante e remove espaços em branco
    altura = float(input("Informe a sual altura: ").strip())

    # Lê o sexo do usuário como um número inteiro (1 para masculino, 2 para feminino)
    sexo = int(input("Informe seu sexo (1-MASCULINO / 2-FEMININO): ").strip())

    # Chama a função peso_ideal com a altura e sexo e guarda o resultado
    resultado = peso_ideal(altura, sexo)

    # Imprime o resultado formatado com duas casas decimais
    print(f"\n-> Seu peso ideal é: {resultado:.2f}Kg")


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Chama a função principal
    main()
