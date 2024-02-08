# 05. Escreva um programa que leia três números inteiros correspondentes a três notas de um aluno. Apresente a média
# das três notas, mas, se a terceira nota for superior a 8, o aluno deve ganhar mais um ponto na média. Além disso,
# se a média final, em função do ponto extra, ficar acima de 10 ela deve ser ajustada para 10.

# Define a função 'media' que calcula a média de três notas.
def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


# Define a função 'main', que será chamada quando o programa for executado.
def main():
    # Solicita ao usuário para inserir as três notas e as converte em números inteiros.
    nota1 = float(input("Insira a primeira nota: ").strip())
    nota2 = float(input("Insira a segunda nota: ").strip())
    nota3 = float(input("Por fim, insira a terceira nota: ").strip())

    # Calcula a média das notas.
    media_notas = media(nota1, nota2, nota3)

    # Se a terceira nota for maior que 8, acrescenta 1 ponto à média.
    if nota3 > 8:
        media_notas += 1

    # Se a média calculada for maior que 10, ajusta para 10.
    if media_notas > 10:
        media_notas = 10

    # Imprime a média final.
    if media_notas != 10:
        print(f"\n-> Sua média final: {media_notas:.2f}")
    else:
        print(f"-> Sua média final: {media_notas}")


# Verifica se o script está sendo executado diretamente (não importado como um módulo).
if __name__ == '__main__':
    # Chama a função 'main' para iniciar a execução do programa.
    main()
