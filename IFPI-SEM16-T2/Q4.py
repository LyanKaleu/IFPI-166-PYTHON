# Função para contar as ocorrências de cada face de um dado
def contar_faces_dado():
    contagem_faces = {}  # Dicionário para armazenar a contagem de cada face
    total_lancamentos = 0  # Contador para o número total de lançamentos

    while True:  # Loop para registrar os resultados dos lançamentos
        resultado = int(input("Digite o resultado do lançamento do dado (ou 0 para encerrar): ").strip())  # Solicita o resultado do lançamento

        if resultado == 0:  # Se o resultado for 0, encerra o loop
            break

        # Incrementa a contagem para a face correspondente no dicionário
        contagem_faces[resultado] = contagem_faces.get(resultado, 0) + 1
        total_lancamentos += 1  # Incrementa o contador de lançamentos

    return total_lancamentos, contagem_faces  # Retorna o número total de lançamentos e a contagem de faces


# Função para mostrar os resultados dos lançamentos do dado
def mostrar_resultados(total_lancamentos, contagem_faces):
    resultado_final = {}  # Dicionário para armazenar o resultado final

    for face in range(1, 7):  # Loop de 1 a 6 para as faces do dado
        resultado_final[face] = contagem_faces.get(face, 0)  # Obtém a contagem de cada face ou 0 se não houver

    print(f"Número total de lançamentos: {total_lancamentos} - Resultados: {resultado_final}")


def main():
    total_lancamentos, contagem_faces = contar_faces_dado()  # Chama a função para contar as faces do dado
    mostrar_resultados(total_lancamentos, contagem_faces)  # Mostra os resultados dos lançamentos do dado


if __name__ == '__main__':
    main()  # Chama a função principal
