# 04. O número da sorte de uma pessoa é calculado somando os dígitos da sua data de nascimento. Escreva um
# programa que leia a data de nascimento, digitada no formado ddmmaaaa (um número inteiro com 8
# dígitos), e mostre o seu número da sorte. Por exemplo, quem nasceu em 29/04/1989 deve digitar 29041989
# e o programa vai calcular que o número da sorte é 42 (2 + 9 + 0 + 4 + 1 + 9 + 8 + 9 = 42).

def numero_sorte(data_nascimento):
    soma = 0
    for digito in str(data_nascimento):
        soma += int(digito)

    return soma


def main():
    data_nascimento = int(input('Digite sua data de nascimento (no formato DDMMAAAA): ').strip())
    numero_da_sorte = numero_sorte(data_nascimento)
    print(f"Seu número da sorte é: {numero_da_sorte}")


if __name__ == '__main__':
    main()
