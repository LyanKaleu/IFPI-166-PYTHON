# Função para cadastrar pessoas
def cadastrar_pessoas():
    pessoas = {}  # Dicionário para armazenar informações das pessoas
    for _ in range(20):  # Loop para cadastrar 20 pessoas
        nome = input("Digite o nome da pessoa: ").strip()  # Solicita o nome da pessoa
        idade = int(input("Digite a idade da pessoa: ").strip())  # Solicita a idade da pessoa
        cpf = input("Digite o CPF da pessoa: ").strip()  # Solicita o CPF da pessoa
        pessoas[cpf] = {'Nome': nome, 'Idade': idade}  # Adiciona os dados ao dicionário usando o CPF como chave
    return pessoas  # Retorna o dicionário de pessoas


# Função para separar as pessoas por idade (maiores ou menores de 18 anos)
def separar_menores(pessoas):
    menores = {}  # Dicionário para armazenar informações das pessoas menores de 18 anos
    maiores = {}  # Dicionário para armazenar informações das pessoas maiores de 18 anos

    for cpf, dados in pessoas.items():  # Loop para verificar a idade de cada pessoa no dicionário
        if dados['Idade'] < 18:  # Verifica se a idade é menor que 18 anos
            menores[cpf] = dados  # Adiciona à lista de menores
        else:
            maiores[cpf] = dados  # Adiciona à lista de maiores

    return maiores, menores  # Retorna dois dicionários, um para maiores e outro para menores


# Função para imprimir os dados das pessoas
def imprimir_dicionarios(dicionario):
    for chave, valor in dicionario.items():
        print(f"{valor['Nome']};{valor['Idade']};{chave}")  # Imprime nome, idade e CPF


def main():
    cadastro = cadastrar_pessoas()  # Realiza o cadastro das pessoas
    maiores_idade, menores_idade = separar_menores(cadastro)  # Separa as pessoas por idade

    print("========== MAIORES DE 18 ANOS ==========")
    imprimir_dicionarios(maiores_idade)  # Imprime os dados das pessoas maiores de 18 anos

    print("========== MENORES DE 18 ANOS ==========")
    imprimir_dicionarios(menores_idade)  # Imprime os dados das pessoas menores de 18 anos


if __name__ == '__main__':
    main()  # Chama a função principal
