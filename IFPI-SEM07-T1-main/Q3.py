# 03. Escreva um programa que leia a cor de um sinal de trânsito (“V” é verde; “A” é amarelo; “E” é vermelho) e retorne
# a respectiva mensagem “Siga”, “Atenção”, ou “Pare”. Assuma entradas válidas.

# Define a função 'semaforo' que determina a ação com base na cor do semáforo.
def semaforo(cor):
    if cor == 'V':
        return 'Siga'
    elif cor == 'A':
        return 'Atenção'
    elif cor == 'E':
        return 'Pare'
    else:
        return 'Sinal de trânsito inválido'


# Define a função 'main', que será chamada quando o programa for executado.
def main():
    # Solicita ao usuário para inserir uma letra representando uma cor de semáforo e converte para maiúsculas.
    cor = input(
        "-=-=-=-=-=SEMÁFORO-=-=-=-=-=\n'V' -> VERDE\n'A' -> AMARELO\n'E' -> VERMELHO\n\nSelecione a opção: ").strip().upper()

    # Chama a função 'semaforo' com a cor fornecida e imprime a ação correspondente.
    print(f"\n A cor selecionada significa: {semaforo(cor)}!")


# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == '__main__':
    # Chama a função 'main' para iniciar a execução do programa.
    main()
    
