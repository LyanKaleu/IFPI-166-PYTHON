# 04. Um número é, por definição, primo se ele não tem divisores, exceto 1 e ele próprio. Escreva um programa
# que leia um número e determine se ele é ou não primo.

def verificar_primo(numero):
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def main():
    num = int(input('Digite um número inteiro qualquer: ').strip())
    if verificar_primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")


if __name__ == '__main__':
    main()
