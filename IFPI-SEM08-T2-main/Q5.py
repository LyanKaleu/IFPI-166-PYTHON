# Define uma função chamada media_escolar que calcula a média escolar
def media_escolar(nota1, nota2, nota3, media_exercicios):
    # Calcula a média final usando a fórmula fornecida
    media_final = (nota1 + (nota2 * 2) + (nota3 * 3) + media_exercicios) / 7

    # Retorna a média final formatada com duas casas decimais
    return f"{media_final:.2f}"


# Define uma função chamada conceito que determina o conceito com base na média final
def conceito(media_final):
    if media_final >= 9.0:
        return "A"
    else:
        if 7.5 <= media_final < 9.0:
            return "B"
        else:
            if 6.0 <= media_final < 7.5:
                return "C"
            else:
                if 4.0 <= media_final < 6.0:
                    return "D"
                else:
                    if media_final < 4.0:
                        return "E"


# Define uma função chamada aprovacao que determina se o aluno foi aprovado ou reprovado
def aprovacao(c):
    if c in "ABC":
        return "Aprovado"
    else:
        if c in "DE":
            return "Reprovado"


# Função principal do programa
def main():
    # Lê a matrícula do aluno, removendo espaços em branco
    matricula = input("Informe a sua matrícula: ").strip()

    # Lê as notas e a média de exercícios do aluno como números de ponto flutuante
    nota1 = float(input("Informe a nota 1: ").strip())
    nota2 = float(input("Informe a nota 2: ").strip())
    nota3 = float(input("Informe a nota 3: ").strip())
    media_exercicios = float(input("Por fim, informe a sua média das notas obtidas nos exercícios: ").strip())

    # Chama a função media_escolar para calcular a média final e guarda o resultado
    resultado_media = media_escolar(nota1, nota2, nota3, media_exercicios)

    # Chama a função conceito para determinar o conceito com base na média final e guarda o resultado
    resultado_conceito = conceito(float(resultado_media))

    # Chama a função aprovacao para determinar se o aluno foi aprovado ou reprovado e guarda o resultado
    resultado_aprovacao = aprovacao(resultado_conceito)

    # Imprime a matrícula, a média final, o conceito e a decisão de aprovação/reprovação
    print(f"\n-> MATRÍCULA: {matricula}")
    print(f"-> MÉDIA FINAL: {resultado_media}")
    print(f"-> CONCEITO: {resultado_conceito}")
    print(f"-> SITUAÇÃO: {resultado_aprovacao}")


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Chama a função principal
    main()
