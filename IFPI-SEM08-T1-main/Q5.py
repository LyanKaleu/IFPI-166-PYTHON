# 05. O índice de massa corporal (IMC) é uma medida internacional usada para calcular se uma pessoa está no peso
# ideal. O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está
# em quilogramas e a altura em metros. Escreva um programa que leia a massa (o peso) e a altura de uma pessoa e
# calcula o IMC de uma pessoa, e depois, mostra uma das seguintes mensagens:
#
# IMC Classificação
# < 18,5 Abaixo do peso
# < 25 Peso normal
# < 30 Sobrepeso
# < 35 Obeso leve
# < 40 Obeso moderado
# >=40 Obeso mórbido

# Define a função 'calcular_imc' que calcula o IMC e determina a categoria correspondente.
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"\n-> O IMC é: {imc:.2f}")

    # Determina a categoria do IMC e retorna a descrição correspondente.
    if imc < 18.5:
        return 'Abaixo do peso'
    else:
        if 18.5 < imc < 25:
            return 'Peso normal'
        else:
            if 25 < imc < 30:
                return 'Sobrepeso'
            else:
                if 30 < imc < 35:
                    return 'Obeso leve'
                else:
                    if 35 < imc < 40:
                        return 'Obeso moderado'
                    else:
                        if imc >= 40:
                            return 'Obeso mórbido'


def main():
    # Solicita e lê o peso e a altura do usuário.
    peso = float(input("Digite o peso (em kg): ").strip())
    altura = float(input("Digite a altura (em metros): ").strip())

    # Chama a função 'calcular_imc' com os dados lidos e imprime a categoria do IMC.
    categoria_imc = calcular_imc(peso, altura)
    print(f"-> Categoria IMC: {categoria_imc}")


# Executa a função 'main' quando o script é executado diretamente.
if __name__ == '__main__':
    main()
