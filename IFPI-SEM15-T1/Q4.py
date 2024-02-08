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


# Esta função identifica as cidades com população maior que o valor informado.
def cidades_maior_populacao(cidades, populacao):
    print(f"\nCIDADES COM MAIS DE {populacao} HABITANTES:")
    # Percorre todas as cidades e verifica aquelas com população superior à informada.
    for cidade in cidades:
        if cidade[5] > populacao:
            # Exibe informações da cidade que atende à condição.
            print(f"IBGE: {cidade[1]} - {cidade[2]}({cidade[0]}) - POPULAÇÃO: {cidade[5]}")


def main():
    # Carrega os dados das cidades do arquivo CSV.
    cidades = carrega_cidades()

    # Solicita ao usuário a população para filtrar as cidades.
    populacao = int(input("Digite o número da população desejado: ").strip())

    # Chama a função para identificar as cidades com população superior à informada.
    cidades_maior_populacao(cidades, populacao)


if __name__ == '__main__':
    main()
