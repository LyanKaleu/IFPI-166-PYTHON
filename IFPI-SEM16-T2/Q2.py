# Importa a biblioteca 'unicodedata' para lidar com caracteres especiais
import unicodedata


# Função para remover acentos de caracteres em um texto
def remover_acentos(texto):
    # Utiliza a função 'normalize' da biblioteca 'unicodedata' para normalizar os caracteres (NFD) e remove os acentos (Mn)
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')


# Função para calcular a frequência das letras em um texto
def calcular_frequencia(texto):
    texto = remover_acentos(texto).upper()  # Remove acentos e converte para maiúsculas
    frequencia = {}  # Dicionário para armazenar a frequência das letras

    for caracter in texto:  # Loop para cada caractere no texto
        if caracter.isalpha():  # Verifica se o caractere é uma letra
            if caracter in frequencia:  # Verifica se a letra já está no dicionário de frequência
                frequencia[caracter] += 1  # Incrementa a contagem da letra
            else:
                frequencia[caracter] = 1  # Adiciona a letra ao dicionário de frequência com contagem 1

    return frequencia  # Retorna o dicionário de frequência das letras


def main():
    texto = input("Digite um texto: ").strip()  # Solicita ao usuário para inserir um texto
    frequencia_letras = calcular_frequencia(texto)  # Calcula a frequência das letras no texto inserido
    print(frequencia_letras)  # Imprime o dicionário com a frequência das letras


if __name__ == '__main__':
    main()  # Chama a função principal
