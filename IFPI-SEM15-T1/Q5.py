# Esta função carrega os dados das cidades de um arquivo CSV e os armazena em uma lista de tuplas.
def carrega_cidades():
    resultado = []
    # Abre o arquivo 'cidades.csv' para leitura.
    with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
        # Lê cada linha do arquivo e separa os valores usando ';' como delimitador.
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            # Adiciona uma tupla com os valores separados na lista 'resultado'.
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()  # Fecha o arquivo.
    return resultado  # Retorna a lista de tuplas com os dados das cidades.


# Esta função identifica as cidades com população maior que o valor informado e que fazem aniversário no mês dado.
def cidades_maior_populacao_e_aniversario(cidades, mes, populacao):
    meses = ['', 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    # Solicita ao usuário um mês e uma população mínima para filtrar as cidades.
    print(f"\nCIDADES COM MAIS DE {populacao} HABITANTES E ANIVERSÁRIO EM {meses[mes].upper()}:")
    # Percorre todas as cidades e verifica aquelas com população superior à informada e aniversário no mês indicado.
    for cidade in cidades:
        if cidade[4] == mes and cidade[5] > populacao:
            # Exibe informações da cidade que atende às condições especificadas.
            print(f"{cidade[2]}({cidade[0]}) tem {cidade[5]} habitantes e faz aniversário em {cidade[3]} de {meses[mes]}.")


def main():
    # Carrega os dados das cidades do arquivo CSV.
    cidades = carrega_cidades()

    # Solicita ao usuário um número correspondente a um mês.
    mes = int(input("Digite o número do mês desejado: ").strip())
    # Solicita ao usuário a população mínima para filtrar as cidades.
    populacao = int(input("Digite a população mínima desejada: ").strip())

    # Chama a função para identificar as cidades com população superior à informada e que fazem aniversário no mês indicado.
    cidades_maior_populacao_e_aniversario(cidades, mes, populacao)


if __name__ == '__main__':
    main()
