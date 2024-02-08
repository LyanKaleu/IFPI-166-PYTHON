# 04. Escreva um programa que leia um caractere e mostra uma das mensagens: “vogal”, “consoante”, “número” ou
# “símbolo”. Observação: O cedilha “ç”, caracteres acentuados, espaço em branco e outros como “símbolo”.

# Define a função 'verificar_caractere' que determina o tipo do caractere fornecido.
def verificar_caractere(caractere):
    if 'A' <= caractere <= 'Z' and caractere in 'AEIOU':
        return 'vogal'
    elif 'A' <= caractere <= 'Z' and caractere not in 'AEIOU':
        return 'consoante'
    elif '0' <= caractere <= '9':
        return 'número'
    else:
        return 'símbolo'


# Define a função 'main', que será chamada quando o programa for executado.
def main():
    # Solicita ao usuário para inserir um caractere e converte para maiúsculas.
    caractere = input("Insira um caractere do teclado: ").strip().upper()

    # Chama a função 'verificar_caractere' com o caractere fornecido e imprime o tipo correspondente.
    print(f"\n-> O tipo de caractere fornecido é um(a): {verificar_caractere(caractere)}")


# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == '__main__':
    # Chama a função 'main' para iniciar a execução do programa.
    main()
    
