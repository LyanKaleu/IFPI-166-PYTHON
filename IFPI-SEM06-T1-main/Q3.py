# 03. Escreva um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e
# exiba esse tempo em horas, minutos e segundos (HH:MM:SS).

# Esta função recebe um valor em segundos
def converter_tempo(segundos):
    # Calcula o restante dos segundos após um dia completo, utilizando a operação de módulo
    segundos = segundos % (24 * 3600)

    # Calcula o número de horas, minutos e segundos usando divisões inteiras e atualiza o valor de 'segundos' para o
    # restante
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60

    # Retorna a string formatada no padrâo HH:MM:SS
    return f"{horas}:{minutos}:{segundos}"


# Essa função é o programa principal
def main():
    # Solicita ao usuário que insira a quantidade de segundos
    segundos = int(input("Digite a quantidade de segundos: ").strip())

    # O resultado retornado pela função 'converter_tempo' é armazenado na variáveç 'resultado'
    resultado = converter_tempo(segundos)

    # Imprime uma mensagem formatada exibindo os segundos originais e o tempo convertido
    print(f"{segundos} segundos é igual a: {resultado}")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
