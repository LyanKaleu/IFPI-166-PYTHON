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


# Esta função identifica as cidades que fazem aniversário em um determinado dia e mês.
def cidades_aniversario(cidades, dia, mes):
    # Lista com os nomes dos meses.
    meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    # Exibe uma mensagem informando as cidades que fazem aniversário na data inserida.
    print(f"\nCIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {meses[mes].upper()}:")
    aniversariantes = []  # Lista para armazenar os nomes das cidades que fazem aniversário.

    # Verifica cada cidade para identificar aquelas que fazem aniversário na data informada.
    for cidade in cidades:
        if cidade[3] == dia and cidade[4] == mes:
            aniversariantes.append(f"{cidade[2]}({cidade[0]})")  # Adiciona o nome da cidade e sua UF à lista.

    return aniversariantes  # Retorna a lista com os nomes das cidades que fazem aniversário.


def main():
    # Carrega os dados das cidades do arquivo CSV.
    cidades = carrega_cidades()

    # Solicita ao usuário o dia e o mês para identificar os aniversariantes.
    dia = int(input("Digite o dia para verificar os aniversariantes das cidades: ").strip())
    mes = int(input("Digite o número do mês (1 a 12) para verificar os aniversariantes das cidades: ").strip())

    # Chama a função para identificar as cidades que fazem aniversário na data informada.
    aniversariantes = cidades_aniversario(cidades, dia, mes)

    # Se houver cidades aniversariantes, exibe seus nomes.
    if aniversariantes:
        for cidade in aniversariantes:
            print(cidade)


if __name__ == '__main__':
    main()
