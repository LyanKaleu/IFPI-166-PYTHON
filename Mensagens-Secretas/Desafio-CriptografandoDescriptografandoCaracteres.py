alfabeto = "abcdefghijklmnopqrstuvwxyz"

chave1 = 7
chave2 = 4
chave3 = 12

letra1 = 'd'
letra2 = 'x'
mensagem = 'omqemd'

posicao1 = alfabeto.find(letra1)
posicao2 = alfabeto.find(letra2)

novaPosicao1 = (posicao1 + chave1) % 26
novaPosicao2 = (posicao2 + chave2) % 26

letraCriptografada1 = alfabeto[novaPosicao1]
letraCriptografada2 = alfabeto[novaPosicao2]

print(f"Sua letra D criptografada é {letraCriptografada1}")
print(f"Sua letra X criptografada é {letraCriptografada2}")

# Descriptografando a mensagem
mensagemDescriptografada = ''
for letra in mensagem:
    if letra in alfabeto:
        posicaoOriginal = alfabeto.find(letra)
        novaPosicao = (posicaoOriginal - chave3) % 26
        letraDescriptografada = alfabeto[novaPosicao]
        mensagemDescriptografada += letraDescriptografada
    else:
        mensagemDescriptografada += letra

print(f"Sua mensagem descriptografada é: {mensagemDescriptografada}")
