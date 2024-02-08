from operator import itemgetter  # Importa a função itemgetter para ordenação

# Dicionário para armazenar os tempos dos corredores
tempos_corredores = {}

# Solicitação dos tempos de cada corredor
for i in range(5):  # Loop para cada corredor
    nome_corredor = input("Digite o nome do corredor: ").strip()  # Solicita o nome do corredor
    tempos = []

    for j in range(5):  # Loop para os tempos de cada volta
        tempo = float(input(f"Digite o tempo da volta {j+1} para {nome_corredor}: ").strip())  # Solicita o tempo de cada volta
        tempos.append(tempo)
    tempos_corredores[nome_corredor] = tempos  # Armazena os tempos do corredor no dicionário

# Cálculo do tempo total, tempo médio e melhor volta de cada corredor
classificacao = []  # Lista para armazenar informações sobre cada corredor
for nome, tempos in tempos_corredores.items():  # Loop para cada corredor e seus tempos
    tempo_total = round(sum(tempos), 1)  # Calcula o tempo total
    tempo_medio = round(sum(tempos) / len(tempos), 1)  # Calcula o tempo médio
    melhor_volta = round(min(tempos), 1)  # Encontra a melhor volta
    classificacao.append((nome, tempo_total, tempo_medio, melhor_volta))  # Adiciona informações à lista

# Ordenação da classificação pelo tempo total
classificacao.sort(key=itemgetter(1))  # Ordena a classificação pela posição 1, que é o tempo total

# Apresentação da classificação final
print(f"-------|------------------|-------------|-------------|--------------")
print(f" Ordem | Nome do Corredor | Tempo Total | Tempo Médio | Melhor Volta ")
print(f"-------|------------------|-------------|-------------|--------------")
for idx, (nome, total, medio, melhor) in enumerate(classificacao, start=1):  # Loop para mostrar a classificação
    print(f"{idx:^7}|{nome:^18}|{total:^13}|{medio:^13}|{melhor:^14}")  # Imprime informações sobre cada corredor
print(f"-------|------------------|-------------|-------------|--------------")
