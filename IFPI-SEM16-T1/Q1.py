# Função para criar um dicionário a partir da entrada do usuário.
def criar_dicionario():
    dicionario = {}

    # Loop para ler chave e valor até que a chave seja vazia
    while True:
        chave = input("Digite a chave (ou deixe em branco para parar): ").strip()
        if chave == '':
            break

        valor = input("Digite o valor: ").strip()
        dicionario[chave] = valor

    return dicionario


# Função para atualizar o valor de uma chave existente no dicionário
def atualizar_valor(dicionario):
    while True:
        chave = input("Digite a chave para atualizar (ou deixe em branco para parar): ").strip()
        if chave == '':
            break

        if chave in dicionario:
            novo_valor = input("Digite o novo valor: ").strip()
            dicionario[chave] = novo_valor
        else:
            print("Chave não encontrada. Tente novamente.")


# Função para mostrar o dicionário na tela
def mostrar_dicionario(dicionario):
    print("\n-> DICIONÁRIO ATUAL:")
    print(dicionario)


def main():
    # Criar o dicionário inicial
    print("-> CRIAÇÃO DO DICIONÁRIO INICIAL")
    dicionario = criar_dicionario()

    # Mostrar o dicionário inicial
    mostrar_dicionario(dicionario)

    # Atualizar valores no dicionário
    print("\nATUALIZAÇÃO DO DICIONÁRIO")
    atualizar_valor(dicionario)

    # Mostrar o dicionário atualizado
    mostrar_dicionario(dicionario)


if __name__ == '__main__':
    main()
