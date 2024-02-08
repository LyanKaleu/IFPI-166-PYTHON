# Função para criar a agenda com um número específico de contatos
def criar_agenda(tamanho_agenda):
    agenda = {}  # Dicionário para armazenar os contatos

    # Loop para adicionar contatos à agenda com um código sequencial como chave
    for codigo in range(1, tamanho_agenda + 1):
        nome = input("Digite o nome do contato: ").strip()  # Solicita o nome do contato
        cidade = input("Digite a cidade do contato: ").strip()  # Solicita a cidade do contato
        estado = input("Digite o estado do contato: ").strip()  # Solicita o estado do contato
        telefone = input("Digite o telefone do contato: ").strip()  # Solicita o telefone do contato

        # Armazena os dados do contato no dicionário usando um código sequencial como chave
        agenda[codigo] = {
            'Nome': nome,
            'Cidade': cidade,
            'Estado': estado,
            'Telefone': telefone
        }

    return agenda  # Retorna a agenda com os contatos


# Função para mostrar a agenda na tela
def mostrar_agenda(agenda):
    for codigo, dados_contato in agenda.items():
        nome = dados_contato['Nome'].ljust(25)  # Ajusta o nome para ocupar 25 caracteres
        cidade = dados_contato['Cidade']  # Obtém a cidade do contato
        estado = dados_contato['Estado']  # Obtém o estado do contato
        telefone = dados_contato['Telefone'].rjust(40 - len(cidade) - len(estado) - 2)  # Ajusta o telefone

        print(f"{nome}{cidade}({estado}){telefone}")  # Imprime os detalhes do contato formatados


def main():
    tamanho = int(input("Insira a quantidade de contatos da agenda: ").strip())  # Solicita o tamanho da agenda
    agenda = criar_agenda(tamanho)  # Cria a agenda com o tamanho especificado
    print("============ CONTATOS ============")
    mostrar_agenda(agenda)  # Mostra a agenda na tela


if __name__ == '__main__':
    main()  # Chama a função principal
