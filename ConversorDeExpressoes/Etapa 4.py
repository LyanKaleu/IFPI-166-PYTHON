def displayMenu():
    print("trdtr de exprss")
    print("=" * 13)
    print("Menu:")
    print("  c = converter uma frase")
    print("  p = imprimir dicionário")
    print("  a = adicionar uma palavra")
    print("  d = remover uma palavra")
    print("  q = sair")


# --------------------------------------------

def convertSentence():
    sentence = input("Insira uma frase para traduzir: ").lower()
    translatedSentence = ""

    # Remove a pontuação da frase
    for char in '?!.,':
        sentence = sentence.replace(char, '')

    # Divide a frase em uma lista de palavras
    listOfWords = sentence.split()

    for word in listOfWords:
        # Adiciona a palavra traduzida se ela existir no dicionário
        if word in textSpeakDictionary:
            translatedSentence += textSpeakDictionary[word] + " "

        # Mantém a palavra original caso não exista tradução
        else:
            translatedSentence += word + " "

    # Imprime a frase traduzida
    print("==>")
    print(translatedSentence)


# ------------------------------------------

def addDictionaryItem():
    txtToAdd = input("Insira a expressão a ser adicionada ao dicionário: ")
    if txtToAdd not in textSpeakDictionary:
        meaning = input("O que ela significa? ")

        # Adiciona a nova tradução ao dicionário
        textSpeakDictionary[txtToAdd] = meaning
    else:
        print("A palavra já existe no dicionário!")


# ------------------------------------------

def deleteDictionaryItem():
    txtToDelete = input("Insira a expressão a ser removida ao dicionário: ")

    if txtToDelete in textSpeakDictionary:
        # Remove a tradução do dicionário
        del textSpeakDictionary[txtToDelete]
    else:
        print("A palavra não existe no dicionário!")


# -----------------------------------------
# O programa principal começa aqui!
# -----------------------------------------

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

running = True

displayMenu()

# Repete até que o usuário digite 'q' para sair
while running:
    menuChoice = input(">_").lower()

    # 'c' para converter
    if menuChoice == 'c':
        convertSentence()

    # 'p' para imprimir
    elif menuChoice == 'p':
        print(textSpeakDictionary)

    # 'a' para adicionar
    elif menuChoice == 'a':
        addDictionaryItem()

    # 'd' para remover
    elif menuChoice == 'd':
        deleteDictionaryItem()

    # 'q' para sair
    elif menuChoice == 'q':
        running = False

    else:
        print("Escolha inválida!")

