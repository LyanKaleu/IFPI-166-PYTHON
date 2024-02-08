# 01. Você sabia que os computadores amam contar coisas? Eles são como pequenos nerds! Vamos fazer um contador
# de letras. Peça ao usuário para digitar uma frase qualquer e, em seguida, imprima o número de caracteres nessa
# frase sem considerar espaços em branco no início ou final da frase digitada.

# Esta função recebe uma string como argumento e retorna o número de caracteres(letras) na string usando a função
# 'len()'
def contador_letras(frase):
    return len(frase)


# Essa função é o programa principal
def main():

    # Utiliza 'input()' para obter uma frase do usuário. Em seguida, chama a função 'contador_letras' com a frase
    # fornecida como argumento
    letras = contador_letras(input("Digite uma frase qualquer: ").strip())

    # Imprime o resultado com a mensagem formatada
    print(f"\n-> A frase possui {letras} letras!")


# Verifica se o script está sendo executado diretamente(não importado como um módulo em outro script)
if __name__ == '__main__':
    main()
