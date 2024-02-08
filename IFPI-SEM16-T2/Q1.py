# Importando a função 'normalize' da biblioteca 'unicodedata' para tratamento de caracteres especiais
from unicodedata import normalize


# Função para contar as vogais em um texto
def contar_vogais(texto):
    # Dicionário para armazenar a contagem de cada vogal, considerando diferentes acentuações
    vogais = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'Á': 0, 'É': 0, 'Í': 0, 'Ó': 0, 'Ú': 0, 'Ã': 0, 'Õ': 0, 'Â': 0,
              'Ê': 0, 'Î': 0, 'Ô': 0, 'Û': 0}

    # Normaliza o texto para o formato 'NFKD' e converte para maiúsculas para garantir a contagem correta
    texto = normalize('NFKD', texto).upper()

    # Loop para percorrer cada caractere do texto e contar as vogais
    for caractere in texto:
        if caractere in vogais:
            vogais[caractere] += 1

    return vogais  # Retorna o dicionário com a contagem de vogais


def main():
    # Solicita ao usuário para inserir um texto
    texto = " ".join(input("Digite um texto: ").split())  # Remove espaços extras no texto
    resultado = contar_vogais(texto)  # Chama a função para contar as vogais no texto inserido

    # Lista das vogais a serem impressas
    vogais_para_imprimir = ['A', 'E', 'I', 'O', 'U']

    print("\n-> QUANTIDADE DE VOGAIS NO TEXTO:")

    # Loop para imprimir a contagem de cada vogal do texto inserido
    for vogal in vogais_para_imprimir:
        print(f"{vogal}: {resultado.get(vogal, 0)}")  # Imprime a vogal e sua contagem (ou 0 se não encontrada)


if __name__ == '__main__':
    main()  # Chama a função principal
