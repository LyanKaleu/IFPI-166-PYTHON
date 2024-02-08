# 01. Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de
# nascimento de uma pessoa, calcule e escreva a idade exata em anos

# Define a função 'calcular_idade' que recebe as informações de data de nascimento e data atual.
def calcular_idade(diaAtual, mesAtual, anoAtual, diaNasc, mesNasc, anoNasc):
    # Calcula a idade subtraindo o ano de nascimento do ano atual.
    idade = anoAtual - anoNasc

    # Verifica se o mês atual é menor que o mês de nascimento.
    if mesAtual < mesNasc:
        # Se o mês atual é menor, subtrai 1 da idade, pois o aniversário ainda não ocorreu.
        idade -= 1
    else:
        # Se o mês atual não é menor, significa que o aniversário já ocorreu ou está ocorrendo este mês.

        # Verifica se o mês atual é igual ao mês de nascimento.
        if mesAtual == mesNasc:
            # Se o mês atual é igual, verifica se o dia atual é menor que o dia de nascimento.
            if diaAtual < diaNasc:
                # Se o dia atual é menor, subtrai 1 da idade, pois o aniversário ainda não ocorreu.
                idade -= 1

    # Retorna a idade calculada.
    return idade


# Define a função 'main' que realiza a entrada de dados e imprime a idade calculada.
def main():
    # Lê o dia, mês e ano atuais do usuário.
    dia_atual = int(input("Digite o dia atual: ").strip())
    mes_atual = int(input("Digite o mês atual: ").strip())
    ano_atual = int(input("Digite o ano atual: ").strip())

    # Lê o dia, mês e ano de nascimento do usuário.
    dia_nascimento = int(input("\nDigite o seu dia de nascimento: ").strip())
    mes_nascimento = int(input("Digite o seu mês de nascimento: ").strip())
    ano_nascimento = int(input("Por fim, digite o seu ano de nascimento: ").strip())

    # Chama a função 'calcular_idade' com os dados lidos e armazena o resultado em 'idade'.
    idade = calcular_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento)

    # Imprime a idade calculada.
    print(f"\n-> Sua idade é: {idade} anos!")


# Executa a função 'main' quando o script é executado diretamente.
if __name__ == '__main__':
    main()
