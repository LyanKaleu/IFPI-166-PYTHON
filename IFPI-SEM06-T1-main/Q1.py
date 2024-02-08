# 01. Escreva um programa que leia um nome pelo teclado e informe quantos caracteres o nome possui.

# Função recebe uma string 'nome' como entrada
def quantos_chr(frase):
    # Retorna o comprimento da string 'nome', ou seja, o número de caracteres que ela possui
    return len(frase)


# Essa função é o programa principal
def main():
    # Solicita ao usuário que insira uma string, chamando a função 'quantos_chr' com a string inserida como argumento
    frase = quantos_chr(input("Digite uma frase qualquer: ").strip())
    # Imprime o resultado
    print(f"A quantidade de caracteres dessa frase é {frase} letras")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
