import random

# Embaralhar as letras no alfabeto
alfabeto = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(alfabeto)
alfabeto = ''.join(alfabeto)

mensagem = input("Por favor, entre com a mensagem a ser criptografada:").lower()
mensagemCriptografada = ""

chave = int(input("Por favor, entre a chave: "))

for char in mensagem:
    if char in alfabeto:
        posicao = alfabeto.find(char)
        # Adicionar um valor aleatório entre 1 e 10 à posição
        novaPosicao = (posicao + chave + random.randint(1, 10)) % 26
        mensagemCriptografada += alfabeto[novaPosicao]
    else:
        mensagemCriptografada += char

# Remover espaços e outros caracteres da mensagem criptografada
mensagemCriptografada = ''.join(filter(lambda char: char.isalpha(), mensagemCriptografada))

print(f"Sua mensagem criptografada é: {mensagemCriptografada}")
