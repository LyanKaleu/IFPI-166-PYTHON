# 01. Escreva um programa que leia o nome e o sexo de uma pessoa, e mostre o nome precedido da mensagem “Ilmo
# Sr.”, caso seja informado o sexo masculino, ou “Ilma Sra.” se for informado o sexo feminino. Use o número inteiro
# 1 para identificar masculino e 2 para identificar feminino.

# Define a função 'get_sexo' que recebe um argumento 'sexo'.
def get_sexo(sexo):
    # Verifica se o valor de 'sexo' é igual a 1.
    if sexo == 1:
        # Retorna a string 'Ilmo Sr.' se a condição for verdadeira.
        return 'Ilmo Sr.'
    elif sexo == 2:
        # Retorna a string 'Ilma Sra.' se a condição for verdadeira.
        return 'Ilma Sra.'
    else:
        # Retorna 'Sexo inválido' se nenhuma das condições anteriores for atendida.
        return 'Sexo inválido'


# Define a função 'main', que será chamada quando o programa for executado.
def main():
    # Solicita ao usuário para digitar seu nome e atribui o valor à variável 'nome'.
    nome = input("Digite seu nome: ").strip()

    # Solicita ao usuário para informar seu sexo (1 para MASCULINO, 2 para FEMININO) e converte o input em um número inteiro.
    sexo = int(input("Informe seu sexo [1-MASCULINO / 2-FEMININO]\n"))

    # Utiliza a função 'get_sexo' para obter o tratamento de gênero adequado e imprime uma saudação.
    print(f"Prazer, {get_sexo(sexo)} {nome}")


# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == '__main__':
    # Chama a função 'main' para iniciar a execução do programa.
    main()
  
