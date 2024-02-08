textSpeakDictionary = {
    "rs": "risos",
    "tmb": "também"
}

# Imprime o dicionário inteiro
print("Dicionário =", textSpeakDictionary)

# Imprime apenas o conteúdo relacionado à chave "rs"
print("\nrs =", textSpeakDictionary["rs"])

# Texto que pede a entrada do usuário
key = input("\nO que você gostaria de converter? ")
print(key, "=", textSpeakDictionary[key])
