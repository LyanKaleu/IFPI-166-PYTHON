# 3. Escreva um programa que leia um número n. Considere uma lista com n posições, e então:
# a) preencha com valores reais lidos pelo teclado e imprima na ordem inversa. Considere até 4 (quatro)
# casas decimais.
# b) preencha com n notas lidas pelo teclado e imprima as notas e a média na tela. Considere 1 (uma) casa
# decimal. Se n = 0, imprima “SEM NOTAS”.
# c) preencha com n letras lidas pelo teclado e imprima quantas vogais foram lidas. Imprima as consoantes.
# Dica: certifique-se de ler apenas um caractere com input()[0]


def lista_inversa(n):
    lista = []
    for i in range(n):
        valor = float(input("Digite um valor real: ").strip())  # Solicita que o usuário digite um valor real
        lista.insert(0, valor)  # Insere o valor no início da lista (ordem inversa)

    return lista  # Retorna a lista preenchida na ordem inversa


def notas_e_media(n):
    notas = []
    if n == 0:
        return f"{notas}\nSEM NOTAS"  # Retorna "SEM NOTAS" se 'n' for zero

    soma = 0
    for i in range(n):
        nota = float(input("Digite uma nota: ").strip())  # Solicita que o usuário digite uma nota
        notas.append(nota)  # Adiciona a nota à lista de notas
        soma += nota  # Soma as notas inseridas

    media = soma / n  # Calcula a média das notas
    return notas, f"{media:.1f}"  # Retorna as notas e a média com uma casa decimal


def lista_caracteres(n):
    vogais = "AEIOUaeiou"
    cont_vogais = 0
    letras = []
    consoantes = []
    for i in range(n):
        letra = input("Digite uma letra: ").strip()  # Solicita que o usuário digite uma letra
        if letra and ('a' <= letra <= 'z' or 'A' <= letra <= 'Z'):
            letra = letra[0]
            letras.append(letra)  # Adiciona a letra à lista de letras lidas

            if letra in vogais:
                cont_vogais += 1  # Conta as vogais

    for letra in letras:
        if ('a' <= letra <= 'z' or 'A' <= letra <= 'Z') and letra not in vogais:
            consoantes.append(letra)  # Adiciona as consoantes à lista

    return cont_vogais, consoantes  # Retorna a contagem de vogais e as consoantes


def main():
    n = int(input("Digite a quantidade de elementos: ").strip())  # Solicita que o usuário digite a quantidade de elementos
    print("Lista na ordem inversa:", lista_inversa(n))  # Imprime a lista preenchida na ordem inversa
    if n == 0:
        resultado_notas = notas_e_media(n)
        print(resultado_notas)  # Imprime "SEM NOTAS" se a quantidade de elementos for zero
    else:
        notas, media = notas_e_media(n)
        print("Notas inseridas:", notas)  # Imprime as notas inseridas
        print("Média das notas:", media)  # Imprime a média das notas
    vogais, consoantes = lista_caracteres(n)
    print("Quantidade de vogais:", vogais)  # Imprime a quantidade de vogais lidas
    print("Consoantes:", consoantes)  # Imprime as consoantes lidas


if __name__ == '__main__':
    main()  # Chama a função principal
