textSpeakDictionary = {
    "rs": "risos",
    "tmb": "também",
    "vc": "você"
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
