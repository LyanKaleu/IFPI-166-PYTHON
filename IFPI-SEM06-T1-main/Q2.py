# 02. Escreva um programa que leia um único caractere pelo teclado e informe o código numérico correspondente ao
# caractere lido.

# A função recebe um caractere como entrada e usa a função ord() para converter o caractere em seu código
# numérico na tabela de caracteres Unicode
def chr_para_codigo(caractere):
    # Retorna o valor numérico resultante
    return ord(caractere)


# Essa função é o programa principal
def main():
    # Solicita ao usuário que insira um caractere, chamando a função 'chr_para_codigo' com o caractere inserido como
    # argumento e imprime o código numérico correspondente
    print(chr_para_codigo(input("Informe um caractere qualquer: ").strip()))


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
