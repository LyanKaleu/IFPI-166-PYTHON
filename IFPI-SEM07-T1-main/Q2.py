# 02. Escreva um programa que leia um número e mostra o valor booleano True (verdadeiro) se o número for ímpar ou
# o valor booleano False (falso) caso contrário.

# Define a função 'eh_impar' que verifica se um número 'n' é ímpar.
def eh_impar(n):
    return n % 2 != 0


# Define a função 'main', que será chamada quando o programa for executado.
def main():
    # Solicita ao usuário para digitar um número inteiro e converte o input em um número inteiro.
    num = int(input("Digite um número inteiro qualquer: ").strip())

    # Verifica se o número é ímpar usando a função 'eh_impar' e imprime o resultado.
    print(f"\n\nO NÚMERO É ÍMPAR?\n-> RESPOSTA: {eh_impar(num)}")


# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == '__main__':
    # Chama a função 'main' para iniciar a execução do programa.
    main()
    
