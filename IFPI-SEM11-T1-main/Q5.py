# 05. Pedro recebe um salário mensal e tem aumentos salariais de 5% uma vez por ano no mês de março. Pedro
# também tem uma dívida no cartão de crédito com uma taxa de juros de 15% ao mês. Considerando que a
# situação se refere ao mês de outubro do ano de 2016, faça um programa leia o valor do salário e o valor
# da dívida e calcula, simulando a evolução do salário e da dívida de Pedro, em que mês e ano a dívida com
# o cartão de crédito será superior ao seu próprio salário.
# Represente os meses como inteiros de 1 a 12.
# Dica: Controle essas quatro variáveis:
# “dívida” que aumenta todo mês;
# “salário” que aumenta apenas se o número do mês for 3 (março);
# “mês” que é incrementado sempre, mas que retorna a 1 quando passar de 12;
# “ano” que só é incrementado quando o mês retornar a 1.
#
# Por exemplo: Considerando que o salário inicial é de R$ 2.000,00 e o valor da dívida é R$ 100,00 o valor
# da dívida irá superar o salário em setembro de 2018 (9/2018)

# Define uma função chamada 'simular_evolucao_salario_divida' que recebe dois argumentos: 'salario_inicial' e
# 'divida_inicial'.
def simular_evolucao_salario_divida(salario_inicial, divida_inicial):
    # Inicializa as variáveis 'salario' e 'divida' com os valores iniciais fornecidos.
    salario = salario_inicial
    divida = divida_inicial

    # Define o mês e o ano inicial.
    mes = 10
    ano = 2016

    # Inicia um loop que continua até a dívida ser maior ou igual ao salário.
    while divida <= salario:
        # Incrementa o mês.
        mes += 1

        # Se o mês ultrapassar 12, incrementa o ano e volta para janeiro.
        if mes > 12:
            mes = 1
            ano += 1

        # Aumenta o salário em 5% no mês de março.
        if mes == 3:
            salario *= 1.05

        # Aumenta a dívida em 15% todo mês.
        divida *= 1.15

    # Retorna o mês e o ano em que a dívida se torna maior que o salário.
    return mes, ano


# Define a função principal chamada 'main'.
def main():
    # Solicita ao usuário o salário inicial.
    salario_inicial = float(input('-> Digite o salário inicial: ').strip())

    # Solicita ao usuário a dívida inicial.
    divida_inicial = float(input('-> Digite a dívida inicial: ').strip())

    # Chama a função 'simular_evolucao_salario_divida' com os valores fornecidos e armazena o resultado em 'mes' e 'ano'.
    mes, ano = simular_evolucao_salario_divida(salario_inicial, divida_inicial)

    # Imprime o mês e ano em que a dívida se torna maior que o salário.
    print(f"\n-> A DÍVIDA SE TORNARÁ MAIOR QUE O SALÁRIO EM: {mes}/{ano}")


# Verifica se este script está sendo executado diretamente.
if __name__ == '__main__':
    # Se sim, chama a função 'main' para iniciar a execução do programa.
    main()
