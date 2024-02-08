# 04. Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
# • o maior número lido;
# • o menor número lido;
# • a média aritmética dos números lidos.

# Esta função retorna o maior número entre os cinco números dados como argumento
def retorna_maximo(num1, num2, num3, num4, num5):
    return max(num1, num2, num3, num4, num5)


# Esta função retorna o menor número entre os cinco números dados como argumento
def retorna_minimo(num1, num2, num3, num4, num5):
    return min(num1, num2, num3, num4, num5)


# Esta função calcula e retorna a média aritmética dos cinco números dados como argumento
def calcular_media(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5


# Essa função é o programa principal
def main():

    # Lê cinco números inteiros e os armazena nas variáveis 'num1', 'num2', 'num3', 'num4', 'num5'
    num1 = int(input("Digite o primeiro número inteiro: ").strip())
    num2 = int(input("Digite o segundo número inteiro: ").strip())
    num3 = int(input("Digite o terceiro número inteiro: ").strip())
    num4 = int(input("Digite o quarto número inteiro: ").strip())
    num5 = int(input("Por fim, digite o quinto número inteiro: ").strip())

    # Chama as funções 'retorna_maximo', 'retorna_minimo' e 'calcular_media' com esses números como argumentos e
    # imprime os resultados
    print(f"\n\n-> MAIOR NÚMERO LIDO: {retorna_maximo(num1, num2, num3, num4, num5)}")
    print(f"-> MENOR NÚMERO LIDO: {retorna_minimo(num1, num2, num3, num4, num5)}")
    print(f"-> MÉDIA ARITMÉTICA DOS NÚMEROS: {calcular_media(num1, num2, num3, num4, num5)}")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
