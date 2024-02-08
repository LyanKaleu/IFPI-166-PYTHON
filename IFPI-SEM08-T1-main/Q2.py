# 02. Escreva um programa que leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva
# qual delas é a mais recente.

# Define a função 'comparar_datas' que compara duas datas.
def comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2):
    # Compara os anos
    if ano1 > ano2:
        return f"{dia1}/{mes1}/{ano1}"
    else:
        if ano1 < ano2:
            return f"{dia2}/{mes2}/{ano2}"
        # Se os anos são iguais, compara os meses

    # Compara os meses
    if mes1 > mes2:
        return f"{dia1}/{mes1}/{ano1}"
    else:
        if mes1 < mes2:
            return f"{dia2}/{mes2}/{ano2}"
        # Se os meses são iguais, compara os dias

    # Compara os dias
    if dia1 > dia2:
        return f"{dia1}/{mes1}/{ano1}"
    else:
        if dia1 < dia2:
            return f"{dia2}/{mes2}/{ano2}"
        else:
            return f"{dia1}/{mes1}/{ano1}"
        # Se os dias são iguais, retorna a primeira data


def main():
    # Solicita e lê os dados da primeira data
    dia1 = int(input("Digite o dia da primeira data: ").strip())
    mes1 = int(input("Digite o mês da primeira data: ").strip())
    ano1 = int(input("Digite o ano da primeira data: ").strip())

    # Solicita e lê os dados da segunda data
    dia2 = int(input("\nDigite o dia da segunda data: ").strip())
    mes2 = int(input("Digite o mês da segunda data: ").strip())
    ano2 = int(input("Digite o ano da segunda data: ").strip())

    # Chama a função 'comparar_datas' com os dados lidos e armazena o resultado em 'resultado'.
    resultado = comparar_datas(dia1, mes1, ano1, dia2, mes2, ano2)

    # Imprime a data mais recente.
    print(f"\n-> A data mais recente é: {resultado}")


# Executa a função 'main' quando o script é executado diretamente.
if __name__ == '__main__':
    main()
