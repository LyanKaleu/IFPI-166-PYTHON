# Função para ler os dados de vendas de diferentes fabricantes ao longo de seis anos.
def ler_dados():
    # Lista de fabricantes pré-definidos.
    fabricantes = ["Fiat", "Ford", "GM", "Wolkswagen"]
    dados = {}  # Dicionário vazio para armazenar os dados.

    # Loop para cada fabricante.
    for fabricante in fabricantes:
        # Pede ao usuário as vendas para cada ano de 2013 a 2018 para o fabricante atual.
        vendas = [int(input(f"Informe as vendas para o fabricante {fabricante} no ano {ano}: ")) for ano in
                  range(2013, 2019)]
        dados[fabricante] = vendas  # Armazena as vendas para o fabricante no dicionário.

    return dados  # Retorna o dicionário com os dados de vendas.


# Função para determinar o fabricante que mais vendeu em um ano específico.
def fabricante_mais_vendeu_ano(dados, ano):
    # Cria um dicionário com as vendas de cada fabricante no ano específico.
    vendas_ano = {fabricante: dados[fabricante][ano - 2013] for fabricante in dados}
    # Encontra o fabricante que teve o maior número de vendas.
    fabricante_mais_vendido = max(vendas_ano, key=vendas_ano.get)
    quantidade_vendida = vendas_ano[fabricante_mais_vendido]  # Quantidade de vendas do fabricante mais vendido.
    return fabricante_mais_vendido, quantidade_vendida


# Função para encontrar o ano com o maior volume geral de vendas.
def ano_maior_volume_vendas(dados):
    # Calcula o total de vendas de todos os fabricantes para cada ano.
    total_anual = {ano: sum(dados[fabricante][ano - 2013] for fabricante in dados) for ano in range(2013, 2019)}
    # Encontra o ano com o maior volume de vendas.
    ano_maior_volume = max(total_anual, key=total_anual.get)
    volume_maior_ano = total_anual[ano_maior_volume]  # Volume de vendas do ano com maior volume.
    return ano_maior_volume, volume_maior_ano


# Função para calcular a média anual de vendas de cada fabricante.
def media_anual_vendas(dados):
    # Calcula a média de vendas para cada fabricante.
    medias = {fabricante: sum(dados[fabricante]) / len(dados[fabricante]) for fabricante in dados}
    return medias


# Função principal para gerenciar todo o processo.
def main():
    dados = ler_dados()  # Lê os dados de vendas.

    # Solicita ao usuário um ano específico.
    ano_escolhido = int(input("Digite o ano desejado para análise: "))
    fabricante_mais_vendido, quantidade_vendida = fabricante_mais_vendeu_ano(dados, ano_escolhido)
    print(f"A fabricante que mais vendeu em {ano_escolhido} foi a {fabricante_mais_vendido} com {quantidade_vendida} mil unidades.")

    ano_maior_volume, volume_maior_ano = ano_maior_volume_vendas(dados)
    print(f"O ano de maior volume geral de vendas foi {ano_maior_volume} com {round(volume_maior_ano, 2)} mil unidades.")

    medias = media_anual_vendas(dados)
    print("A média anual de vendas de cada fabricante entre 2013 e 2018 foi:")
    for fabricante, media in medias.items():
        print(f"A {fabricante} vendeu em média {round(media, 2)} unidades por ano.")


if __name__ == "__main__":
    main()  # Chama a função principal.
