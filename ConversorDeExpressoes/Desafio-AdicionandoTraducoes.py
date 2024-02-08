textSpeakDictionary = {
    "rs": "risos",
    "tmb": "também",
    "vc": "você",
    "pq": "porque",
    "btf": "boto fé",
    "ctt": "contato",
    "fds": "fim de semana",
    "flw": "falou",
    "mdm": "melhor do mundo",
    "mds": "Meu Deus",
    "pcr": "parceiro",
    "amg": "amigo",
    "pdc": "pode crer",
    "pft": "perfeito",
    "plmds": "pelo amor de Deus",
    "pprt": "papo reto",
    "pse": "pois é",
    "tlg": "tá ligado",
    "tmj": "tamo junto",
    "agr": "agora",
    "bb": "bebê",
    "bjs": "beijos",
    "blz": "beleza",
    "glr": "galera",
    "msm": "mesmo",
    "ngm": "ninguém",
    "obg": "obrigado",
    "sdds": "saudades",
    "smp": "sempre",
    "td": "tudo",
    "vdd": "verdade",
    "q": "que"
}

# Obtém a frase para tradução
sentence = input("Insira uma frase para traduzir: ").lower()

# Divide a frase em uma lista de palavras
wordsToTranslate = sentence.split()

translatedSentence = ""

# Passa por cada palavra da lista
for word in wordsToTranslate:
    # Adiciona a palavra traduzida caso ela exista no dicionário
    if word in textSpeakDictionary:
        translatedSentence += textSpeakDictionary[word] + " "

    # Mantém a palavra original caso não exista tradução
    else:
        translatedSentence += word + " "

# Imprime a frase traduzida
print("==>")
print(translatedSentence)
