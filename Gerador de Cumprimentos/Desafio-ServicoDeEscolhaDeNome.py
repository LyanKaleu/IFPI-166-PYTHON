from random import choice

nomes_animais = ['Bruthus', 'Pétala', 'Jane', 'Lola', 'Martin']

print("Serviço de escolha de nome para animais de estimação")
print("------------------")

print('''
Menu
    g = gerar um nome aleatório para seu animal
    a = adicionar nome de animal
    r = remover nome de animal
    n = imprimir nomes de animais
    q = sair
''')

while True:
    menuChoice = input("\n>_")

    if menuChoice == 'a':
        tipo_animal = input("Qual o tipo do animal (cachorro, gato, pássaro, etc.)? ")
        genero = input("Qual o gênero do animal (macho ou fêmea)? ")
        nome_animal = input("Digite o nome do animal: ")

        if nome_animal not in nomes_animais:
            if genero.lower() == 'macho':
                nomes_animais.append(nome_animal)
                print(f"O nome do {tipo_animal} macho é {nome_animal}")
            elif genero.lower() == "fêmea":
                nomes_animais.append(nome_animal)
                print(f"O nome da {tipo_animal} fêmea é {nome_animal}")
            else:
                nomes_animais.append(nome_animal)
                print(f"O nome do {tipo_animal} é {nome_animal}")
        else:
            print("Este nome já está na lista.")

    elif menuChoice == 'g':
        print(f"Você deve chamar seu animal de estimação de {choice(nomes_animais)}")

    elif menuChoice == 'r':
        nome_remover = input("Qual nome de animal você gostaria de remover? ")
        if nome_remover in nomes_animais:
            nomes_animais.remove(nome_remover)
            print(f"O nome '{nome_remover}' foi removido da lista.")
        else:
            print("Este nome não está na lista.")

    elif menuChoice == 'n':
        print("Aqui estão os nomes dos animais:")
        for nome in nomes_animais:
            print(nome)

    elif menuChoice == 'q':
        break

    else:
        print("Insira uma opção válida!")
