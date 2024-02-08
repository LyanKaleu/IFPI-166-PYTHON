# Função para ler os anos de nascimento de um número específico de pessoas
def ler_anos_nascimento(numero_pessoas):
    anos = []  # Lista para armazenar os anos de nascimento

    for i in range(numero_pessoas):  # Loop para coletar os anos de nascimento
        ano = int(input("Digite o ano de nascimento da pessoa: ").strip())  # Solicita o ano de nascimento
        anos.append(ano)  # Adiciona o ano à lista

    return anos  # Retorna a lista com os anos de nascimento


# Função para contar a quantidade de pessoas que nasceram em cada ano
def contar_nascimentos(anos):
    contagem_nascimentos = {}  # Dicionário para armazenar a contagem de nascimentos por ano

    for ano in anos:  # Loop para cada ano na lista de anos de nascimento
        if ano in contagem_nascimentos:  # Verifica se o ano já está presente na contagem
            contagem_nascimentos[ano] += 1  # Incrementa a contagem de nascimentos para esse ano
        else:
            contagem_nascimentos[ano] = 1  # Adiciona o ano à contagem com contagem 1

    return contagem_nascimentos  # Retorna o dicionário com a contagem de nascimentos por ano


# Função para exibir a contagem de pessoas por ano de nascimento em ordem cronológica
def exibir_contagem(contagem_nascimentos):
    anos_ordenados = sorted(contagem_nascimentos.keys())  # Obtém os anos em ordem cronológica

    for ano in anos_ordenados:  # Loop para cada ano ordenado
        print(f"Ano {ano}: {contagem_nascimentos[ano]} pessoas")  # Imprime o ano e a contagem de pessoas


def main():
    numero_pessoas = 1000  # Define o número de pessoas para coletar os anos de nascimento

    anos_nascimento = ler_anos_nascimento(numero_pessoas)  # Lê os anos de nascimento das pessoas
    contagem = contar_nascimentos(anos_nascimento)  # Calcula a contagem de nascimentos por ano
    exibir_contagem(contagem)  # Exibe a contagem de pessoas por ano em ordem cronológica


if __name__ == '__main__':
    main()  # Chama a função principal
