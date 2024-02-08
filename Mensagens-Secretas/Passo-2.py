# Uma lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

# Capture a mensagem do usuário
mensagem = input("Por favor, entre com a mensagem a ser criptografada: ").lower()

# Esta variável armazenará a mensagem criptografada
mensagemCriptografada = ""

# Capture a chave secreta
chave = input("Por favor, entre a chave: ")

# Esta ação é necessário porque o programa não lê o valor da chave como número
chave = int(chave)

# Percoora cada caracter na mensagem
for char in mensagem:
    if char in alfabeto:
        # Encontre a posição de caracter em alfabeto, por exemplo, 'a' está na posição 0, 'e' está na posição 4, etc.
        posicao = alfabeto.find(char)

        # Some a chave secreta para encontrar a posição do caracter criptografado
        # % 26 significa 'volte para 0 quando você atingir 26'
        novaPosicao = (posicao + chave) % 26

        # Acrescente a letra descriptografada à mensagem a letra criptografada está em alfabeto na novaPosicao
        mensagemCriptografada += alfabeto[novaPosicao]
    else:
        # Alguns caracteres (por exemplo '$', '?') não estão no alfabeto, então simplestemente adicione a letra
        # criptografada à mensagem
        mensagemCriptografada += char

print(f"Sua mensagem criptografada é: {mensagemCriptografada}")
