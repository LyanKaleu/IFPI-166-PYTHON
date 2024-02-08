# Função para criar e mostrar o dicionário de livros
def criar_dicionario_livros():
    codigo = 101  # Código inicial para os livros
    livros = {}  # Dicionário para armazenar os dados dos livros

    # Loop para ler os dados dos livros
    while True:
        # Ler os dados do livro
        titulo = input("Digite o título do livro (ou deixe em branco para parar): ").strip()
        if not titulo:
            break

        isbn = input("Digite o ISBN do livro: ").strip()
        autor = input("Digite o autor do livro: ").strip()
        preco = float(input("Digite o preço do livro: ").strip())

        # Armazenar os dados do livro no dicionário usando um código sequencial como chave
        livros[codigo] = {
            'Título': titulo,
            'ISBN': isbn,
            'Autor': autor,
            'Preço': preco
        }
        codigo += 1  # Incrementar o código para o próximo livro

    # Mostrar os dados dos livros no formato desejado
    for codigo, dados_livro in livros.items():
        print(f"\nCódigo: {codigo}")
        for campo, valor in dados_livro.items():
            if campo == 'Preço':  # Verifica se o campo é 'Preço' para formatar para duas casas decimais
                valor = f'{valor:.2f}'  # Formata o valor para duas casas decimais
            print(f"{campo}: {valor}")

    return livros


def main():
    print("-> CADASTRO DE LIVROS\n")
    criar_dicionario_livros()


if __name__ == '__main__':
    main()
