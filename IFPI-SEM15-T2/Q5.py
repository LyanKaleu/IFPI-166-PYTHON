# Define uma função para ler os dados de faturamento de várias filiais ao longo de vários anos e meses.
def ler_faturamento():
    filiais = 3  # número de filiais
    meses = 12  # número de meses
    anos = 4  # número de anos
    faturamento = [[[0 for _ in range(meses)] for _ in range(filiais)] for _ in range(anos)]

    # Loop para preencher o faturamento para cada ano, filial e mês.
    for ano in range(anos):
        for filial in range(filiais):
            for mes in range(meses):
                # Solicita ao usuário o valor do faturamento para uma determinada filial, ano e mês.
                valor = int(
                    input(f"Informe o faturamento da filial {filial + 1}, no ano {ano + 2014}, no mês {mes + 1}: "))
                faturamento[ano][filial][mes] = valor  # Armazena o valor do faturamento.

    return faturamento  # Retorna a matriz de faturamento.


# Função para calcular o total de faturamento de uma filial em um ano específico.
def calcular_total_ano_filial(faturamento, ano, filial):
    return sum(faturamento[ano - 2014][filial])


# Função para calcular o total de faturamento de todas as filiais em um ano específico.
def calcular_total_todas_filiais_por_ano(faturamento, ano):
    return sum(calcular_total_ano_filial(faturamento, ano, filial) for filial in range(len(faturamento[0])))


# Função para calcular o total de faturamento de todas as filiais ao longo de todos os anos.
def calcular_total_periodo_todas_filiais(faturamento):
    return sum(calcular_total_todas_filiais_por_ano(faturamento, ano) for ano in range(len(faturamento)))


# Função para exibir os resultados do faturamento das filiais.
def exibir_resultados(faturamento):
    total_periodo_todas_filiais = int()

    # Loop para exibir o faturamento de cada ano, filial e mês.
    for ano in range(len(faturamento)):
        for filial in range(len(faturamento[0])):
            for mes in range(len(faturamento[0][0])):
                # Exibe os valores do faturamento de cada filial, ano e mês.
                print(f"{ano + 2014};Filial {filial + 1};{meses[mes]};{faturamento[ano][filial][mes]}")
            total_ano_filial = calcular_total_ano_filial(faturamento, ano + 2014, filial)
            # Exibe o total do faturamento de cada filial em um determinado ano.
            print(f"TOTAL {ano + 2014} FILIAL {filial + 1};{total_ano_filial}")

        total_todas_filiais_por_ano = calcular_total_todas_filiais_por_ano(faturamento, ano + 2014)
        # Exibe o total do faturamento de todas as filiais em um determinado ano.
        print(f"TOTAL {ano + 2014} TODAS FILIAIS;{total_todas_filiais_por_ano}")
        total_periodo_todas_filiais += total_todas_filiais_por_ano

    # Exibe o total do faturamento de todas as filiais ao longo de todos os anos.
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo_todas_filiais}")


meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
         "Novembro", "Dezembro"]


# Função principal que chama as funções anteriores para ler e exibir o faturamento.
def main():
    faturamento = ler_faturamento()
    exibir_resultados(faturamento)


if __name__ == "__main__":
    main()  # Chama a função principal.
